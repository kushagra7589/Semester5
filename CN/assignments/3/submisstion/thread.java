import java.net.*;
import java.io.*;

class ChatThread extends Thread {
	private Socket clientSocket = null;
	private DataInputStream readInput = null;
	public PrintStream writeOutput = null;
	private ChatThread chatThreads[] = null;
	private int curr;
	private int maxNumberOfClients;
	
	public ChatThread(Socket cs, ChatThread threads[], int i)
	{
		this.clientSocket = cs;
		this.chatThreads = threads;
		this.maxNumberOfClients = this.chatThreads.length;
		this.curr = i;
	}
	
	private String  AcceptName()
	{
		String name = null;
		this.writeOutput.println("Enter your name?");
		try
		{
			name = this.readInput.readLine();
			System.out.println(name);
		}
		catch (IOException e)
		{
			System.out.println("Could not read name.");
		}
		return name;
	}
	
	private void haveConversation(String name)
	{
		try
		{
			while(true)
			{
				String input = this.readInput.readLine();
				if(input.startsWith("exit"))
				{
					return;
				}

				String words[] = input.split("\\s");
				System.out.println("Reversed : ");
				for(int j = words.length - 1; j >= 0; j--)
				{
					System.out.print(words[j] + " ");
				}
				System.out.println();
				synchronized(this)
				{
					for(int i = 0; i < this.maxNumberOfClients; i++)
					{
						if(this.chatThreads[i] != null && i != curr)
						{
							this.chatThreads[i].writeOutput.println(name + " >> " + input);
						}
						if(this.chatThreads[i] != null)
						{
							String words1[] = input.split("\\s");
							this.chatThreads[i].writeOutput.println("Reversed : ");
							for(int j = words1.length - 1; j >= 0; j--)
							{
								this.chatThreads[i].writeOutput.print(words1[j] + " ");
							}
							this.chatThreads[i].writeOutput.println();
						}
					}
				}
			}
		}
		catch (IOException e)
		{
			System.out.println("Could not get input.");
		}
	}
	
	private void leaveChat(String name)
	{
		this.writeOutput.println("Bye " + name);
		System.out.println(name + " is leaving!");
		synchronized(this)
		{
			for(int i = 0; i < this.maxNumberOfClients; i++)
			{
				if(this.chatThreads[i] != null && i != this.curr)
				{
					this.chatThreads[i].writeOutput.println(name + " is leaving!");
				}
			}
		}
		this.chatThreads[this.curr] = null;
	}
	
	
	public void run()
	{
		
		try
		{
			this.readInput = new DataInputStream(this.clientSocket.getInputStream());
			this.writeOutput = new PrintStream(this.clientSocket.getOutputStream());
			String name = null;
			while(name == null)
			{
				name = AcceptName();
			}
			this.writeOutput.println("Welcome " + name + " to the chat server. Write 'exit' to quit from the server");
			
			synchronized(this)
			{
				for(int i = 0; i < this.maxNumberOfClients; i++)
				{
					if(this.chatThreads[i] != null && i != curr)
					{
						this.chatThreads[i].writeOutput.println(name + " has joined!");
					}
				}
			}
			
			this.haveConversation(name);
			
			this.leaveChat(name);
			
			this.readInput.close();
			this.writeOutput.close();
			this.clientSocket.close();
			
			
		}
		catch(IOException e)
		{
			System.out.println("Could not create I/o stream");
		}
		
	}
}