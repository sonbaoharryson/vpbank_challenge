from fastapi import FastAPI
from api.endpoints import router
from services.simulation import simulate_transaction
from storage.memory import add_transaction, get_transactions
import asyncio
import requests
from api.endpoints import convert_to_unlabeled
import json
from typing import List
from azure.servicebus import ServiceBusClient, ServiceBusMessage
import os

app = FastAPI(title="Bank Transaction Simulation API")
app.include_router(router)


async def generate_transactions_periodically(anomaly_rate: float = 0.5):
    while True:
        i=0
        while i<2:
            txn = simulate_transaction(anomaly_rate)
            add_transaction(txn)
            i+=1
        unlabeled_transaction = [convert_to_unlabeled(txn) for txn in get_transactions()]
        transactions_dict = [txn.dict() for txn in unlabeled_transaction]
        transactions_json = json.dumps(transactions_dict, ensure_ascii=False, indent=4)
        # Forward to AWS API Gateway
        #try:
            #aws_api_url = os.environ.get("AWS_API_URL")
            # if isinstance(payload["timestamp"], datetime):
            #     payload["timestamp"] = payload["timestamp"].isoformat()

            #req = requests.post(
             #   aws_api_url,
              #  json=transactions_dict,
               # headers={"Content-Type": "application/json"}
            #)
            #req.raise_for_status()
            #if req.status_code == 200:
            #    print(f"Transaction {transactions_dict} forwarded to AWS successfully.")
        #except Exception as e:
        #    print(f"Failed to forward to AWS: {e}")
        #    print(transactions_json)

        # Forward to Fabric EventStream
        entity_path = None
        connection_string = os.environ.get("FABRIC_CONNECTION_STRING")
        for param in connection_string.split(';'):
            if param.startswith('EntityPath='):
                entity_path = param.split('=')[1]
                break
            
        if not entity_path:
            raise ValueError("EntityPath is missing in the connection string. Please check you Fabric setup. Can get the connection string in EventStream after publishing a custom pipeline.")
        
        if isinstance(transactions_json, dict):
            message = [transactions_json]
        
        service_bs_client = ServiceBusClient.from_connection_string(connection_string)
        try:
            with service_bs_client.get_queue_sender(entity_path) as sender:
                batch_message = [ServiceBusMessage(json.dumps(msg)) for msg in message]
                sender.send_messages(batch_message)
                print(f"Successfully send {len(message)} records to EventStream.")
        except Exception as e:
            print(f"Error sending messages: {e}")
        finally:
            service_bs_client.close()

        await asyncio.sleep(10)

@app.on_event("startup")
async def start_background_generation():
    asyncio.create_task(generate_transactions_periodically())
