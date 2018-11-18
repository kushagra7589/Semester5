import java.util.*;

class PairSI
{
	public String x;
	public int y;

	public PairSI()
	{
		this.x = "";
		this.y = 0;
	}

	public PairSI(String x, int y)
	{
		this.x = x;
		this.y = y;
	}

	public String toString()
	{
		return this.x + " : " + this.y;
	}
}

class PairIS
{
	public String y;
	public int x;

	public PairIS()
	{
		this.x = 0;
		this.y = "";
	}

	public PairIS(int x, String y)
	{
		this.x = x;
		this.y = y;
	}
}

class ParseString
{
	private String input;
	private HashMap<String, ArrayList<PairSI> > graph;

	public ParseString(String x)
	{
		this.input = x;
		graph = new HashMap<String, ArrayList<PairSI> >();
	}

	public HashMap<String, ArrayList<PairSI> > makeGraph()
	{
		int i = 0;
		char c;
		int next = 1;
		ArrayList<PairSI> temp1 = new ArrayList<PairSI>();
		ArrayList<PairSI> temp2 = new ArrayList<PairSI>();
		PairSI p = new PairSI();
		PairSI rev = new PairSI();
		String key = "";
		System.out.println(this.input);
		while((c = input.charAt(i)) != '#' && i < this.input.length())
		{
			if(c == ' ')
			{
				i++;
				continue;
			}
			if(next == 1)
			{
				String check = "" + c;
				if(!graph.containsKey(check))
				{
					graph.put(check, new ArrayList<PairSI>());
				}
				temp1 = graph.get(check);
				next = 2;
				key = check;
			}
			else if(next == 2)
			{
				String check  = "" + c;
				if(!graph.containsKey(check))
				{
					graph.put(check, new ArrayList<PairSI>());
				}
				p = new PairSI();
				temp2 = graph.get(check);
				p.x =  "" + c;
				next = 3;
			}
			else if(next == 3)
			{
				String a = "";
				a += c;
				i++;
				while(input.charAt(i) != ' ')
				{
					c = input.charAt(i);
					a += c;
					i++;
				}
				int w = Integer.parseInt(a);
				p.y = w;
				temp1.add(p);
				graph.put(key, temp1);
				
				rev = new PairSI(key, w);
				temp2.add(rev);
				String new_node = p.x; 
				graph.put(new_node, temp2);
				next = 1;
			}
			i++;
		}
		return graph;
	}

	public HashMap<String, ArrayList<PairSI> > updateGraph(String inp)
	{
		String[] splitted = inp.split(" ");
		String x = splitted[0];
		String y = splitted[1];
		Integer w = Integer.parseInt(splitted[2]);

		if(!this.graph.containsKey(x))
		{
			this.graph.put(x, new ArrayList<PairSI>());
		}

		if(!this.graph.containsKey(y))
		{
			this.graph.put(y, new ArrayList<PairSI>());
		}

		ArrayList<PairSI> temp1 = this.graph.get(x);
		ArrayList<PairSI> temp2 = this.graph.get(y);

		int flag = 0;
		for(PairSI p : temp1)
		{
			if(p.x.equals(y))
			{
				temp1.set(temp1.indexOf(p), new PairSI(y, w));
				flag = 1;
			}
		}	
		if(flag == 0)
		{
			temp1.add(new PairSI(y, w));
		}

		flag = 0;
		for(PairSI p : temp1)
		{
			if(p.x.equals(x))
			{
				temp2.set(temp2.indexOf(p), new PairSI(x, w));
				flag = 1;
			}
		}	
		if(flag == 0)
		{
			temp2.add(new PairSI(x, w));
		}

		this.graph.put(x, temp1);
		this.graph.put(y, temp2);

		return this.graph;
 	}

	public static void main(String args[])
	{
		Scanner reader = new Scanner(System.in);
		System.out.println("Input the initial router configuration");
		String input = reader.nextLine();

		ParseString str = new ParseString(input);
		HashMap<String, ArrayList<PairSI> > mp = str.makeGraph();
		System.out.println(Arrays.asList(mp));
		ShortestDistance sd = new ShortestDistance(mp);
		for(String key : mp.keySet())
		{
			sd.dijkstra(key);
		}
		for(String key : mp.keySet())
		{
			sd.bellmanFord(key);
		}
		String check = "y";
		while(check.equals("y"))
		{
			System.out.println("Do you want to update/add any link? [y/n]");
			check = reader.nextLine();
			if(check.equals("n"))
				break;
			System.out.println("Enter the update: ");
			String update = reader.nextLine();
			mp = str.updateGraph(update);
			sd = new ShortestDistance(mp);
			for(String key : mp.keySet())
			{
				sd.dijkstra(key);
			}
			for(String key : mp.keySet())
			{
				sd.bellmanFord(key);
			}		
		}


	}
}

class ShortestDistance
{
	private HashMap<String, ArrayList<PairSI> > graph;
	private HashMap<String, String> routing_table;
	private HashMap<String, HashMap<String, Integer> > dist;

	private HashMap<String, HashMap<String, Integer> > bf_dist;
	private HashMap<String, String> bf_routing_table;

	private final int inf = 100000000;
	public ShortestDistance(HashMap<String, ArrayList<PairSI> > g)
	{
		this.graph = g;
		this.routing_table = new HashMap<String, String>();
		this.bf_routing_table = new HashMap<String, String>();
		this.dist = new HashMap<String, HashMap<String, Integer> >();
		this.bf_dist = new HashMap<String, HashMap<String, Integer> >();
		for(String key : graph.keySet())
		{
			HashMap<String, Integer> curr_dist = new HashMap<String, Integer>();
			HashMap<String, Integer> bf_curr_dist = new HashMap<String, Integer>();
			for(String k : graph.keySet())
			{
				curr_dist.put(k, inf);
				bf_curr_dist.put(k, inf);
			}
			this.dist.put(key, curr_dist);
			this.bf_dist.put(key, bf_curr_dist);
		}
	}

	public void dijkstra(String source)
	{

		// initialising the distance of all vertices as infinity 
		for(String key : graph.keySet())
		{
			HashMap<String, Integer> curr_dist = new HashMap<String, Integer>();
			for(String k : graph.keySet())
			{
				curr_dist.put(k, inf);
			}
			this.dist.put(key, curr_dist);
		}
		System.out.println("LINK STATE FOR ROUTER " + source);

		// implementing dijkstra using priority queue
		PriorityQueue<PairIS> pq = new PriorityQueue<PairIS>(1, new Comparator<PairIS>()
		{
			public int compare(PairIS a, PairIS b)
			{
				return a.x - b.x;
			}
		});

		boolean y = pq.add(new PairIS(0, source));
		HashMap<String, Integer> curr_dist = this.dist.get(source);
		curr_dist.put(source, 0);

		int iteration = 0;

		while(pq.size() > 0)
		{
			String u = pq.poll().y;
			System.out.println("----------------------------------------------------------");
			System.out.println("Current iteration : " + iteration); iteration += 1;
			System.out.println("Node with smallest distance from " + source + " is : " + u + " with distance " + curr_dist.get(u));
			ArrayList<PairSI> adj = graph.get(u);
			int flag = 0;
			for(PairSI i : adj)
			{				
				String v = i.x;
				Integer w = i.y;
				if(curr_dist.get(v) > curr_dist.get(u) + w)
				{
					routing_table.put(v, u);
					int updated = curr_dist.get(u) + w;
					System.out.println("Updating distance of " + v + " from " + curr_dist.get(v) + " to " + updated);
					curr_dist.put(v, updated);
					y = pq.add(new PairIS(curr_dist.get(v), v));
					flag = 1;
				}
			}
			if(flag == 0)
			{
				System.out.println("No updation");
			}
			System.out.println("----------------------------------------------------------");
		}
		ArrayList<PairSI> adj = graph.get(source);

		System.out.println("ROUTING TABLE for " + source);
		for(String dest : graph.keySet())
		{
			String parent = dest;
			System.out.print(dest);
			while(!parent.equals(source))
			{
				parent = routing_table.get(parent);
				System.out.print(" -> " + parent);
			}
			System.out.println("");
		}
		System.out.println("");		
		this.dist.put(source, curr_dist);
	}

	public void bellmanFord(String source)
	{
		System.out.println("BELLMANFORD FOR ROUTER " + source);
		for(String key : graph.keySet())
		{
			HashMap<String, Integer> bf_curr_dist = new HashMap<String, Integer>();
			for(String k : graph.keySet())
			{
				bf_curr_dist.put(k, inf);
			}	
			this.bf_dist.put(key, bf_curr_dist);
		}
		
		HashMap<String, Integer> bf_curr_dist = this.bf_dist.get(source);

		bf_curr_dist.put(source, 0);

		for(int i = 1; i <= this.graph.keySet().size() - 1; i++)
		{
			System.out.println("-----------	-----------------------------------------------");
			System.out.println("Current iteration : " + i);
			for(String ver : this.graph.keySet())
			{
				ArrayList<PairSI> adj = graph.get(ver);
				for(PairSI p : adj)
				{
					String v = p.x;
					String u = ver;
					Integer weight = p.y;
					if(bf_curr_dist.get(u) != inf && bf_curr_dist.get(u) + weight < bf_curr_dist.get(v))
					{
						routing_table.put(v, u);
						Integer updated = bf_curr_dist.get(u) + weight;
						System.out.println("Updating distance of " + v + " from " + bf_curr_dist.get(v) + " to " + updated);
						bf_curr_dist.put(v, bf_curr_dist.get(u) + weight);
					}
				}
			}
			System.out.println("-------------------------------------------------------------");
		}

		System.out.println("ROUTING TABLE for " + source);
		for(String dest : graph.keySet())
		{
			String parent = dest;
			System.out.print(dest);
			while(!parent.equals(source))
			{
				parent = routing_table.get(parent);
				System.out.print(" -> " + parent);
			}
			System.out.println("");
		}
		System.out.println("");		
		this.bf_dist.put(source, bf_curr_dist);
	}
}