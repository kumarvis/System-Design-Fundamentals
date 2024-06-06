# 20  System Design Concepts

## 1. Vertical Scaling
Vertical scaling, also known as "scaling up," involves adding more resources to a single server or machine to handle increased load or performance demands.

![alt text](Resources/20_system_design_concepts/vertical_scaling.png)

**Drawbacks of Vertical Scaling:**

- Finite Limits: There is a limit to how much a single server can be upgraded.
Cost: High-end hardware upgrades can be expensive.
- Risk of Downtime: Potential downtime during hardware upgrades or maintenance
- Single Point of Failure: If the upgraded server fails, the entire application can go down.

## 2. Horizontal Scaling
Horizontal scaling, also known as "scaling out," involves adding more servers or machines to a system to handle increased load or performance demands.

![alt text](Resources/20_system_design_concepts/horizontal_scaling.png)

**Key Characteristics of Horizontal Scaling:**

- Resource Addition: Adding more servers or nodes to the system.
- Distributed Load: Spreads the load across multiple machines, enhancing overall system capacity.
- Scalability: Potentially limitless scalability as more machines can be added as needed.
- Fault Tolerance: Increased redundancy and fault tolerance, as the failure of one node doesn't bring down the entire system.
- Complexity: Requires sophisticated load balancing, data distribution, and often a more complex infrastructure to manage multiple nodes.
- Consistency Challenges: May involve challenges related to data consistency, especially in distributed databases or applications.

## 3. Load Balancer or Reverse Proxy
A load balancer is a device, server or software application that distributes incoming network or application traffic across multiple servers. Load balancers play a crucial role in horizontal scaling by enabling efficient resource utilization and enhancing fault tolerance.

![alt text](Resources/20_system_design_concepts/load_balancer.png)

**Key Functions of a Load Balancer:**

- Traffic Distribution: Distributes incoming requests evenly across multiple servers to prevent any single server from becoming a bottleneck.

- Health Monitoring: Continuously checks the health and status of servers to ensure that only healthy servers receive traffic.

- Failover: Automatically reroutes traffic to healthy servers in the event of a server failure, enhancing system reliability.

- SSL Termination: Offloads SSL decryption from backend servers, improving their performance by reducing computational load.

- Session Persistence: Ensures that a user's session is consistently directed to the same server, which is important for applications requiring session-specific data.

- Traffic Optimization: Can optimize traffic by compressing data, caching responses, or distributing workloads based on server capacity.

**Load Balancing Algorithms:**
- Round Robin: Distributes requests sequentially across all servers.
- Least Connections: Directs traffic to the server with the fewest active connections.
- Least Response Time: Sends requests to the server with the lowest response time.
IP Hash: Routes requests based on the client's IP address, ensuring consistent routing for the same client.
- Weighted Round Robin/Least Connections: Assigns weights to servers based on their capacity, with more powerful servers receiving more traffic.