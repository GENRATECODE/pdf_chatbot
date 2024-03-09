import flet as ft
import asyncio
import  chatbot_function as chat_bot

async def main(page: ft.Page):
    url = "https://mer.vin/2024/01/open-interpreter-use-cases/"
    page.title = "Chatbot"
    page.window_max_height = 880   
    page.window_max_width = 500 
    page.scroll=ft.ScrollMode.HIDDEN
    page.bgcolor= "#CA955C" 
    new_message = ft.TextField(label="Prompt",border_color="#17594A" ,hint_text="Please enter Your Qurey",icon=ft.icons.ANDROID,bgcolor="#17594A")
    chat = ft.Column(
        spacing=10,
        width=260,    
        height=620,  
        scroll=ft.ScrollMode.HIDDEN,  
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment = ft.CrossAxisAlignment.START,   
    )
    Output=ft.Column(
        spacing=10,         
        width=230,
        height=620,  
        scroll=ft.ScrollMode.HIDDEN,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment = ft.CrossAxisAlignment.START,
    ) 
    async def bot_input(question):
        try:  
            result  = chat_bot.ask(question)                
            Output.controls.append(        
            ft.Text(f"{result['result']}\n MetaData\n {result['source']}"))    
            await page.update_async()  # Update the page after appending the text

        except Exception as e:
            print(f"Error in bot_input: {e}") 
    async def send_click(e):
            
        chat.controls.append(      
            ft.Text(f"User 👤->{new_message.value}", color=ft.colors.BLUE)
        )
        await page.update_async()
        await asyncio.create_task(bot_input(new_message.value))
        new_message.value = ""   
        await page.update_async()
        # Use await page.update_async() instead for asynchronous updates

    # Add the message to the chat
    row = ft.Row(controls=[new_message, ft.ElevatedButton("Send", on_click=send_click)]    )
    
    # Await page.add_async to ensure the UI is updated
    row_output=ft.Row(controls=[Output,chat])
    # Await page.add_async to ensure the UI is updated    
    title=ft.Text("Chatbot ",size=40, text_align=ft.TextAlign.END,color="Blue")     
    await page.add_async(title,row_output,row) 

if __name__ == "__main__":
    ft.app(target=main)

