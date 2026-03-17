import asyncio

async def wait_for_connection(drone, timeout=10):
    print("Aguardando conexão com drone...")

    start_time = asyncio.get_event_loop().time()

    async for state in drone.core.connection_state():
        if state.is_connected:
            print("Drone conectado!")
            return True

        # verifica timeout
        if asyncio.get_event_loop().time() - start_time > timeout:
            print("[TIMEOUT] Não conectou no drone")
            return False

        await asyncio.sleep(0.5)