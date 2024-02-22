# Import the module
import asyncio

# Function to count upto 1 based on parameter
async def countdown(n):
    while n > 0:
        print(n)
        await asyncio.sleep(1)
        n -= 1  
    print(n)

# Main function to run the async function
async def main():
    num = int(input("Enter a number: "))
    await asyncio.gather(countdown(num))

# Call the main function
asyncio.run(main())
print("All threads execution has been completed!")