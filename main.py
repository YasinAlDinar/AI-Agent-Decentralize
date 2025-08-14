import sys
import asyncio
from uagents import Agent, Context
from uagents.setup import fund_agent_if_low
from interfaces.interactive import interactive_mode

# Inisialisasi Agent
pharmacy_agent = Agent(
    name="pharmacy_finder",
    port=8000,
    seed="bhdjwkfpvfjkamsbcgtdyqkfogtsbsmkcpwkdpp",
    endpoint=["http://127.0.0.1:8000/submit"],
)

# Fund agent jika saldo rendah
fund_agent_if_low(pharmacy_agent.wallet.address())

@pharmacy_agent.on_event("startup")
async def startup_event(ctx: Context):
    ctx.logger.info(f"🏥 Pharmacy Finder Agent started!")
    ctx.logger.info(f"Agent address: {pharmacy_agent.address}")
    ctx.logger.info("Ready to help find pharmacies and medicines!")

if __name__ == "__main__":
    print("🏥 Starting Pharmacy Finder Agent...")
    print(f"Agent Address: {pharmacy_agent.address}")

    # Cek apakah mode interaktif diaktifkan
    if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
        # Jalankan mode interaktif
        asyncio.run(interactive_mode())
    else:
        # Jalankan agent normal
        print("🚀 Agent is running... Press Ctrl+C to stop")
        print("💡 Tip: Gunakan --interactive untuk mode testing")
        pharmacy_agent.run()