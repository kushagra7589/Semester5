import java.net.*;
import java.io.*;

class ChatServer {
	private ServerSocket serverSocket = null;
	private Socket clientSocket = null;
	private int maxClients = 10;
	private ChatThread[] chatThreads = new ChatThread[maxClients];
	
	public ChatServer(int port)
	{
		try
		{
			this.serverSocket = new ServerSocket(port);
			for(int i = 0; i < this.maxClients; i++)
			{
				this.chatThreads[i] = null;
			}
		}
		catch (Exception e)
		{
			System.out.println(e);
		}
	}
	
	public static void main(String args[])
	{	
		if(args.length < 1)
		{
			System.out.println("Usage ChatServer <port>");
			return;
		}
		int pno = Integer.parseInt(args[0]);
		ChatServer chatServer = new ChatServer(pno);
		
		int clientNumber = 1;
		while(true)
		{
			try
			{
				chatServer.clientSocket = chatServer.serverSocket.accept();
				System.out.println("Client " + clientNumber + " connected");
				clientNumber++;
				int i = 0;
				for(i = 0; i < chatServer.maxClients; i++)
				{
					if(chatServer.chatThreads[i] == null)
					{
						chatServer.chatThreads[i] = new ChatThread(chatServer.clientSocket, chatServer.chatThreads, i);
						chatServer.chatThreads[i].start();
						break;
					}
				}
				if(i == chatServer.maxClients)
				{
					PrintStream sedlife = new PrintStream(chatServer.clientSocket.getOutputStream());
					sedlife.println("Server Busy. Try again later.");
					sedlife.close();
					chatServer.clientSocket.close();
				}
			}
			catch(IOException e)
			{
				System.out.println(e);
			}
		}
	}
	
}
