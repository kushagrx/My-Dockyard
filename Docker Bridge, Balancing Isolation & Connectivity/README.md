# 🚀 Docker Bridge: Balancing Isolation & Connectivity

## 📌 Objective
The goal of this exercise is to explore and demonstrate network isolation in Docker containers. We’ll examine how containers within the same custom bridge network can communicate, while those on different networks remain isolated. This concept is crucial for securing microservices and containerized applications.

---

## 🌐 Introduction to Docker Networking
Docker networking is fundamental for **containerized applications**, allowing containers to communicate while ensuring **security and isolation**. Docker provides several networking options:

### 🔹 Types of Docker Networks:
- **Bridge Network (Default)** – Allows communication between containers using internal IPs unless restricted.
- **Custom Bridge Network** – Offers better control and supports name-based resolution.
- **Host Network** – Attaches containers directly to the host’s network stack.
- **Overlay Network** – Enables communication across multiple hosts (Docker Swarm).
- **Macvlan Network** – Assigns a MAC address to each container, making them appear as separate devices.
- **None Network** – Completely disables networking.

For this demonstration, we focus on the **custom bridge network**, which improves control and **network isolation**.

---

## ⚡ Why Use a Custom Bridge Network?
A custom bridge network offers several benefits: ✅ Enhanced Security – Containers on different networks are isolated by default.
✅ Better Performance – Direct communication without host stack overhead.
✅ DNS-Based Resolution – Communicate via container names instead of IPs.
✅ Greater Control – Define specific subnets, IP ranges, and gateways.

We’ll create a custom bridge network called kushagra-bridge and connect multiple containers.

---

## 🔧 1. Creating a Custom Bridge Network
```bash
docker network create --driver bridge --subnet 192.168.1.0/24 --ip-range 192.168.1.100/25 kushagra-bridge
```
### 🔍 Explanation:
- `--driver bridge` → Uses the default **bridge network mode**.
- `--subnet 192.168.1.0/24` → Defines the network’s **IP range**.
- `--ip-range 192.168.1.100/25` → Allocates IPs dynamically.

---

## 🚀 2. Running Containers in the Custom Network
### Running **Redis Container** (`tarak-database`)
```bash
docker run -itd --net=kushagra-bridge --name=kushagra-database redis
```
### Running **BusyBox Container** (`tarak-server-A`)
```bash
docker run -itd --net=kushagra-bridge --name=kushagra-server-A busybox
```

### 📌 Check Container IPs
```bash
docker network inspect kushagra-bridge
```
Expected Output:
```
kushagra-database: 192.168.1.100  
kushagra-server-A: 192.168.1.101  

```

---

## 🔄 3. Testing Communication Between Containers
### Ping from **tarak-database** to **tarak-server-A**
```bash
docker exec -it kushagra-database ping 192.168.1.101
```
### Ping from **tarak-server-A** to **tarak-database**
```bash
docker exec -it kushagra-server-A ping 192.168.1.100
```
✅ Expected Outcome: Both containers should successfully **ping** each other.

---

## 🚧 4. Demonstrating Network Isolation with a Third Container
We add another container (`kushagra-server-B`) on the **default bridge network**.
```bash
docker run -itd --name=tarak-server-B busybox
```
### 📌 Get IP of `Kushagra-server-B`
```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' kushagra-server-B
```
(Example IP: `172.17.0.2`)

---

## ❌ 5. Testing Communication Between Different Networks
Ping from `tarak-database` to `tarak-server-B`:
```bash
docker exec -it kushagra-database ping 172.17.0.2
```
🚨 **Expected Outcome:** The ping should **fail**, as they are on different networks.

---

## 🔍 6. Confirming Network Isolation
### Inspect Networks
```bash
docker network inspect kushagra-bridge  
docker network inspect bridge  

```
✅ kushagra-bridge should contain kushagra-database & kushagra-server-A.
✅ bridge should contain kushagra-server-B.

---

## 🏆 Conclusion
- **Containers in the same network** can communicate.
- **Containers in different networks** are isolated **by default**.
- Docker’s **networking model** ensures security and separation unless explicitly connected.

🚀 **Now you have mastered Docker Bridge Networking!** 🎯
