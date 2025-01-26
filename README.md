# A K8 Hello World

If you're bored with the traditional "Hello World," this project is for you!

This project takes the classic "Hello World" and adds a Kubernetes-based twist to it. It sets up multiple components: a PostgreSQL database, a server application, and a client application. Each component is deployed as a separate Kubernetes resource, with configuration and secrets handled securely.

## Assumptions and Prerequisites:

- Docker Desktop with Kubernetes integration enabled. Learn more in the [Docker Desktop Kubernetes documentation](https://docs.docker.com/desktop/features/kubernetes/).
- Project repository cloned to your local machine.
- All commands executed from the `manifests/` directory of the repository.

## Components Created

The following resources will be created in your local cluster:

1. **ConfigMap**:  
   - Stores initialization scripts for creating and seeding a `messages` table in the PostgreSQL database with the "Hello World" message.

2. **PostgreSQL (Database)**:  
   - Hosts the "Hello World" message in the `messages` table.
   - Deployed as a `Deployment` and exposed via a `ClusterIP` or `NodePort` `Service`.
   - Uses Kubernetes `Secrets` for secure user authentication.
   - Initialized with a pre-defined SQL script.

3. **Server Application**:  
   - Acts as an API that retrieves the "Hello World" message from the database.
   - Default configuration creates two replicas (pods) for high availability.
   - Deployed as a `Deployment` and exposed via a `NodePort` `Service` (configurable to `ClusterIP`).
   - Reads database connection details from Kubernetes `Secrets`.

4. **Client Application**:  
   - Fetches and renders the "Hello World" message from the API.
   - Deployed as a `Deployment` and exposed via a `NodePort` `Service`.
   - Communicates with the API using the `SERVER_URL` environment variable.


## How to Use (Setting it up):

### 0. Clone the Repository and Navigate to the Manifests Directory

Before running the commands, ensure you have cloned the repository and moved into the correct directory. For example:

```bash
git clone https://github.com/brettenet/hello-ps-k8.git
```
```bash
cd hello-ps-k8/manifests
```

### 1. Create your secrets 
   A wise person once said, "Security first." Follow these steps to create your Kubernetes secrets securely. Be sure to replace the example values with your actual data before running the commands:
   
   ```bash
   kubectl create secret generic postgres-username-secret --from-literal=POSTGRES_USER=postgres
   ```

   ```bash
   kubectl create secret generic postgres-password-secret --from-literal=POSTGRES_PASSWORD=securepassword
   ```

### 2a. Apply All Resources at Once

All the YAML files (e.g., ConfigMaps, Deployments, Services) are located in the same directory. You can apply them in a single step. Navigate to the manifests/ directory and run the following command:

```bash
kubectl apply -f .
```

### 2b. Alternatively Apply Individually

If you prefer to apply each deployment manually from the manifests/ directory, run the following commands:

**ConfigMaps**
```bash
kubectl apply -f postgres-init-config.yaml
```

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
Look for the STATUS column. It should display Running for all 4 pods.

**Getting your First Hello World:**

Open your favorite browser and navigate to the client.
```bash
http://localhost:30000
```
