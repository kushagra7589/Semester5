import java.io.*;
import java.net.*;
import java.util.*;
import java.lang.*;

class Client
{
	private DatagramSocket clientSocket;
	private InetAddress ipAddress;
	private byte[] received;
	private byte[] to_send;
	private int portNo;
	private int nextSeqNumber;
	private int window_size;

	public Client(int portNo)
	{
		try
		{
			this.ipAddress = InetAddress.getByName("localhost");
			this.received = new byte[1024];
			this.to_send = new byte[1024];
			this.portNo = portNo;
			this.nextSeqNumber = 0;
			this.window_size = 1;
		}
		catch (UnknownHostException e)
		{
			System.out.println("localhost could not be resolved");
		}
	}

	public void send_and_receive_packets(ArrayList<Packet> packetList, int serverPno)
	{
		while(true)
		{
			try
			{
				System.out.println("--------------- Starting with window size : " + this.window_size + "-------------------");

				/*---- create socket for this window ----*/
				this.clientSocket = new DatagramSocket(this.portNo);
				this.clientSocket.setSoTimeout(4000);

				/*---- set duplicate ACK counter ----*/
				int dup_ack_count = 0;
				
				/*---- create bytes array for this window and send the packets ---*/
				int i;
				for(i = nextSeqNumber; i < nextSeqNumber + window_size; i++)
				{
					Packet p = packetList.get(i);
					to_send = Packet.getBytes(p);
					System.out.println("Sending packet " + p.getSequenceNo());
					DatagramPacket dp_send = new DatagramPacket(to_send, to_send.length, this.ipAddress, serverPno);
					this.clientSocket.send(dp_send);
				}

				/*---- receive packets sent by the server ----*/
				int counter = 0;
				while(counter < this.window_size)
				{
					/*---- check whether there is triple ACK ----*/
					if(dup_ack_count == 3)
					{
						System.out.println("A triple ACK has occurred, preparing for retransmisson with half the window size");
						window_size = Math.max(1, window_size/2);
						for(int j = nextSeqNumber; j < nextSeqNumber + window_size; j++)
						{
							Packet p = packetList.get(j);
							p.setCorrect();
						}
					}

					DatagramPacket dp_recv = new DatagramPacket(received, received.length);
					this.clientSocket.receive(dp_recv);
					received = dp_recv.getData();
					Packet recv_packet = (Packet)Packet.getObject(received);
					int recv_seq_no = recv_packet.getSequenceNo();
					System.out.println("ACK received for " + recv_seq_no);
					if(recv_seq_no == nextSeqNumber)
					{
						System.out.println("This was the expected packet!");
						nextSeqNumber += 1;
						counter += 1;
					}
					else if(recv_seq_no == nextSeqNumber - 1)
					{	
						System.out.println("This was duplicate ack!");
						dup_ack_count += 1;
					}
				}
				this.window_size += 1;
				this.clientSocket.close();
				System.out.println("-----------This window was successfully sent!-----------");
			}
			catch(SocketTimeoutException e)
			{
				System.out.println("The window has timed out. Preparing for retransmission with window size = 1");
				this.window_size = 1;
				for(int j = nextSeqNumber; j < nextSeqNumber + window_size; j++)
				{
					Packet p = packetList.get(j);
					p.setCorrect();
				}
				this.clientSocket.close();
			}
			catch(SocketException e)
			{
				System.out.println("The socket could not be created!");
				this.clientSocket.close();
				break;
			}
			catch(IOException e)
			{
				System.out.println("There was error in sending/receiving data");
				this.clientSocket.close();
				break;
			}
			catch(Exception e)
			{
				this.clientSocket.close();
				break;
			}
		}
	}

	public static void main(String args[])
	{
		if(args.length < 2)
		{
			System.out.println("Usage : client.java clientPortNo ServerPortNo");
		}
		int clno = Integer.parseInt(args[0]);
		int serverpno = Integer.parseInt(args[1]);

		Client client = new Client(clno);

		ArrayList<Packet> packetList = new ArrayList<Packet>();

		for(int i = 0; i < 5000; i++)
		{
			Packet p = new Packet(1, i);
			packetList.add(p);
		}

		Random rand = new Random();

		int range = 10;

		Random rand1 = new Random(); 

		for(int i = 0; i < 500; i++)
		{
			int j = rand.nextInt(range);
			int x = rand1.nextInt(3);
			range += 10;
			Packet p = packetList.get(j);
			if(x == 0 || x == 1)
				p.setCorrupt();
			else
				p.setLost();
		}

		client.send_and_receive_packets(packetList, serverpno);

		for(String a : args)
		{
			System.out.println(a);
		}
	}

}


