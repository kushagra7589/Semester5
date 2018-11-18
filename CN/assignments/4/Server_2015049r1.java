import java.net.*;
import java.io.*;
import java.util.*;

class ChatRoomServer
{
	private int MAX_CLIENTS = 50;
	private ServerSocket ss;
	private Socket cs;
	private Map<Integer, String> ids;
	private Map<String, Integer> names;
	private ClientThread threads[] = new ClientThread[MAX_CLIENTS];

	public ChatRoomServer(int port)
	{
		try
		{
			this.ss = new ServerSocket(port);
			for(int i = 0; i < this.MAX_CLIENTS; i++)
			{
				this.threads[i] = null;
			}
			ids = new HashMap<Integer, String>();
			names = new HashMap<String, Integer>();
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
			System.out.println("Usage ChatRoomServer <port>");
			return;
		}
		int pno = Integer.parseInt(args[0]);
		ChatRoomServer chatServer = new ChatRoomServer(pno);
		
		// int clientNumber = 1;
		while(true)
		{
			try
			{
				chatServer.cs = chatServer.ss.accept();
				clientNumber++;
				int i = 0;
				for(i = 0; i < chatServer.MAX_CLIENTS; i++)
				{
					if(chatServer.threads[i] == null)
					{
						System.out.println("Client " + i + " connected");
						chatServer.threads[i] = new ClientThread(chatServer.cs, chatServer.threads, chatServer.ids, chatServer.names, i);
						chatServer.threads[i].start();
						break;
					}
				}
				if(i == chatServer.MAX_CLIENTS)
				{
					PrintStream sedlife = new PrintStream(chatServer.cs.getOutputStream());
					sedlife.println("Server Busy. Try again later.");
					sedlife.close();
					chatServer.cs.close();
				}
			}
			catch(IOException e)
			{
				System.out.println(e);
			}
		}
	}
}

class ClientThread extends Thread
{
	private Socket cs;
	private DataInputStream request;
	private PrintStream response;
	private ClientThread cThreads[];
	private Map<Integer, String> ids;
	private Map<String, Integer> names;
	int curr;
	int MAX_CLIENTS;

	public ClientThread(Socket clientSocket, ClientThread ct[], Map<Integer, String> i, Map<String, Integer> n, int c)
	{
		this.cs = clientSocket;
		this.cThreads = ct;
		this.ids = i;
		this.names = n;
		this.MAX_CLIENTS = this.cThreads.length;
		this.curr = c;
	}

	String AcceptName()
	{
		String name = null;
		this.response.println("Enter your username?");
		// name = this.request.readLine();
		try
		{
			name = this.request.readLine();
			System.out.println(name + " has connected");
			if(names.get(name) != null)
			{
				this.response.println("This username has already been taken.");
				return null;
			}
		}
		catch (IOException e)
		{
			System.out.println("Could not read name.");
		}
		return name;
	}	

	private void haveConversation()
	{
		try
		{
			while(true)
			{
				String input = this.request.readLine();
				if(input.startsWith("exit"))
				{
					return;
				}
				else if(input.startsWith("All"))
				{
					String msg = input.split(":")[1].trim();
					synchronized(this)
					{
						for(int i = 0; i < this.MAX_CLIENTS; i++)
						{
							if(this.cThreads[i] != null & i != curr)
							{
								this.cThreads[i].response.println(ids.get(curr) + " >> " + msg);
							}
						}
					}
				}
				else if(input.equals("Server: List All"))
				{
					for(Map.Entry m : ids.entrySet())
					{
						this.response.println(m.getKey() + " : " + m.getValue());
					}
				}
				else if(input.startsWith("Client"))
				{
					String inp[] = input.split(":");				
					String command = inp[0];
					String clients[] = command.split(",");
					int client_list[] = new int[this.MAX_CLIENTS];
					int N = clients.length;
					for(int x = 1; x < N; x++)
					{
						client_list[x] = Integer.parseInt(clients[x].trim());
					}
					client_list[0] = Integer.parseInt(clients[0].split(" ")[1].trim());
					String msg = inp[1].trim();
					// for(int x : client_list)
					// {
					// 	System.out.println(x);
					// }
					synchronized(this)
					{
						for(int j = 0; j < N; j++)
						{
							int x = client_list[j];
							String cli = ids.get(x);
							if(cli == null)
							{
								this.response.println("Client " + x + " is not a part of the chat room");
							}
							else
							{
								this.cThreads[x].response.println(ids.get(curr) + " >> " + msg);
							}
						}
					}
				}
				else
				{
					this.response.println("This is not a valid command!");
				}
			}
		}
		catch (IOException e)
		{
			System.out.println("Could not get input from client(" + ids.get(curr) + ")");
		}
	}

	private void leaveChat()
	{
		synchronized(this)
		{
			this.response.println("Client " + curr + " disconnected.");
			System.out.println("Client " + curr + " disconnected.");
			this.cThreads[this.curr] = null;
			for(int i = 0; i < this.MAX_CLIENTS; i++)
			{
				if(this.cThreads[i] != null && i != this.curr)
				{
					String nme = ids.get(curr);
					this.cThreads[i].response.println(nme + " is leaving!");
				}
			}
			names.remove(ids.get(curr));
			ids.remove(curr);
		}
	}

	public void run()
	{
		try
		{
			this.request = new DataInputStream(this.cs.getInputStream());
			this.response = new PrintStream(this.cs.getOutputStream());
			String name = null;
			while(name == null)
			{
				name = AcceptName();
			}

			this.response.println("Welcome " + name + "! Type 'exit' to leave the chat room.");
			names.put(name, curr);
			ids.put(curr, name);
			this.response.println("You are assigned the id : " + curr);

			synchronized(this)
			{
				for(int i = 0; i < this.MAX_CLIENTS; i++)
				{
					if(this.cThreads[i] != null && i != curr)
					{
						this.cThreads[i].response.println(name + " (id = " + curr + "), has joined the chatroom.");
					}
				}
			}

			this.haveConversation();
			this.leaveChat();

			this.response.close();
			this.request.close();
			this.cs.close();

		}
		catch (IOException e)
		{
			System.out.println(e);
		}
	}
}