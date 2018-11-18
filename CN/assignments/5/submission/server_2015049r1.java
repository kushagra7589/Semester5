import java.io.*;
import java.util.*;
import java.net.*;

class Server
{
	private int pno;
	private DatagramSocket serverSocket;
	private byte[] received;
	private byte[] to_send;
	private InetAddress ipAddress;

	public Server(int pno)
	{
		try
		{
			this.pno = pno;
			this.serverSocket = new DatagramSocket(pno);
			this.ipAddress = InetAddress.getByName("localhost");
			this.received = new byte[1024];
			this.to_send = new byte[1024];
		}
		catch(UnknownHostException e)
		{
			System.out.println("Some excpetion");
		}
		catch(SocketException e)
		{
			System.out.println("Host nahi bana");
		}
	}

	public void send_and_receive()
	{
		try
		{
			int last_seq_received = -1;
			while(true)
			{
				/*---- receive a packet from a client ----*/
				DatagramPacket dp = new DatagramPacket(received, received.length);
				this.serverSocket.receive(dp);

				/*---- get the client's ip and port ----*/
				int client_pno = dp.getPort();
				InetAddress client_ip = dp.getAddress();

				/*---- check sequence number and whether packet is corrupt ----*/
				Packet p = (Packet)Packet.getObject(dp.getData());
				if(p.checkLost())
				{
					System.out.println("Packet " + p.getSequenceNo() + " was lost!");
					continue;
				}
				
				System.out.println("received packet " + p.getSequenceNo());
				if(!p.checkCorrupt())
				{
					if(last_seq_received == p.getSequenceNo() - 1)
						last_seq_received = p.getSequenceNo();
				}

				/*---- send acknowledgement to the server ----*/
				System.out.println("sending ACK");
				Packet ack = new Packet(0, last_seq_received);
				to_send = Packet.getBytes(ack);
				DatagramPacket sendPacket = new DatagramPacket(to_send, to_send.length, client_ip, client_pno);
				this.serverSocket.send(sendPacket);
			}
		}
		catch(Exception e)
		{
			this.serverSocket.close();
		}
	}

	public static void main(String args[])
	{
		if(args.length < 1)
		{
			System.out.println("Usage : server.java serverPortNo");
		}

		int sno = Integer.parseInt(args[0]);

		Server server = new Server(sno);

		server.send_and_receive();
	}
}