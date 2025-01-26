# A Very Much Hello World

If you are board with your traditional 'hello world' this project if for you!

This project takes your traditional boring 'Hello World' and adds a Kubernetes-based twist setup with multiple components: a PostgreSQL database, a server application (api), and a client application. Each component is deployed as a separate Kubernetes resource, with configuration and secrets handled securely.

## Assumptions and Prerequisites:

- This guide assumes that you are using Docker Desktop and have enabled its Kubernetes integration. You can find more information on how to do this in the [Docker Desktop Kubernetes documentation](https://docs.docker.com/desktop/features/kubernetes/).
- Directions assume you have already cloned the project repository to your local machine.
- All commands should be run from the manifests/ directory within the cloned repository.
- Kubernetes must be enabled in Docker Desktop’s settings and configured to run the workloads.
- The user should have kubectl installed and configured to use Docker Desktop’s Kubernetes cluster.
- The images referenced should already be available in docker hub and accessible by the local cluster.
  
## Components
The  following resources will be created in your local cluster.

1. **ConfigMap**:  
   Stores configuration data used by various components, more specifically the initialization scripts that create and seed a  `messages` table in a PostgreSQL database with the wonderful 'Hello World' message. 

2. **PostgreSQL (Database)**:  
   - This is where the source 'Hello World' messages resides.
   - Deployed as a `Deployment` and exposed via a `ClusterIP` `Service` (or `NodePort` if configured).  
   - Handles user and password authentication securely using Kubernetes `Secrets`.  
   - Initialized with a pre-defined SQL script.

3. **Server Application (API)**:  
   - Acts an API that grabs the 'Hello World' message from the database.
   - Default configuration creates 2 replicas (pods) because 'Hello World' should always be highly available.
   - Deployed as a `Deployment` and exposed via a `NodePort` `Service` but could also operate as a `ClusterIP`.  
   - Reads database connection details from environment variables supplied by Kubernetes `Secrets`.  
   - Connects to the database and providing a backend API.

4. **Client Application (Example API Consumer)**:  
   - This is the lucky resource that fetch and renders 'Hello World' from the API.
   - Deployed as a `Deployment` and exposed via a `NodePort` `Service`.  
   - Communicates with the server application through an environment-provided `SERVER_URL`.

## How to Use (Setting it up):

### 0. Clone the Repository and Navigate to the Manifests Directory

Before running the commands, ensure you have cloned the repository and moved into the correct directory. For example:

```bash
git clone https://github.com/your-repo/your-project.git
cd your-project/manifests
```

This step sets the context, ensuring that users start in the correct location.

### 1. Create your secrets:**  
   A wise person once said 'security first'. Please run these these kubectl commands to create your secrets. Replace the example values with your own.
   ```bash
   kubectl create secret generic postgres-username-secret --from-literal=POSTGRES_USER=postgres
   kubectl create secret generic postgres-password-secret --from-literal=POSTGRES_PASSWORD=securepassword
   ```

### 2a. Apply All Resources at Once

All the YAML files (ConfigMap, Deployments, Services) are located in the same directory, you can apply them in a single step. From the `manifests/` directory, run:

```bash
kubectl apply -f .
```

### 2b. Alternatively Apply Individually

If you prefer to run each deployment manually from the `manifests/` directory, you can run these commands:

**Postgres**
```bash
kubectl apply -f postgres-init-config.yaml

**Postgres**
```bash
kubectl apply -f postgres.yaml
```

**Server**
```bash
kubectl apply -f server.yaml
```

**Client**
```bash
kubectl apply -f client.yaml
```

### 3 Verifying That Everything is Running

After applying all the resources, you can verify that the pods and services are running as expected.

**Check All Resources:**
   ```bash
   kubectl get all
   ```

**Getting your First Hello World:**

Open your favorite browser and navigate to the client.
```bash
http://localhost:30001
```