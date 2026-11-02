# Deployed Architecture

## Architecture Diagram

```text
                       +-------------------------------------------------+
                       |                   AWS EC2 Instance              |
                       |               (Ubuntu / t2.micro)               |
                       |                                                 |
  +-------------+      |   +-------------+           +-------------+     |
  |   GitHub    |      |   |   Jenkins   |           |    PM2      |     |
  | Repositories|      |   |  (Port 8080)|           | (Process    |     |
  +-------------+      |   +-------------+           |  Manager)   |     |
         |             |          |                  +-------------+     |
         |             |          |                         |            |
         | Webhook     |          | SSH / Execute           |            |
         | Trigger     |          | Deployment Scripts      |            |
         +-------------+--------->+-------------------------+            |
                       |                                                 |
                       |   +-------------------+    +----------------+   |
                       |   |   Flask Backend   |    | Express Front  |   |
                       |   |   (Port 5000)     |    | (Port 3000)    |   |
                       |   +-------------------+    +----------------+   |
                       +-------------------+----------------+------------+
                                           |                |
                                           |                |
                                +----------+----+  +--------+--------+
                                |  Public IP:   |  |  Public IP:     |
                                |  Port 5000    |  |  Port 3000      |
                                +---------------+  +-----------------+
                                           |                |
                                           v                v
                                      [ User Browser Access ]
```

## Architecture Description

This architecture demonstrates a fully automated CI/CD pipeline deploying two separate applications (a Flask backend and an Express frontend) onto a single Amazon EC2 instance.

### 1. Infrastructure
*   **Provider:** Amazon Web Services (AWS)
*   **Compute:** A single EC2 instance (Ubuntu) is provisioned to host all services.
*   **Security Groups:** Configured to allow inbound traffic on:
    *   Port `22` (SSH for remote access)
    *   Port `3000` (Express Frontend access)
    *   Port `5000` (Flask Backend access)
    *   Port `8080` (Jenkins Web UI access)

### 2. Application Layer
*   **Flask Backend:** Runs on Port `5000`. It handles backend logic and APIs.
*   **Express Frontend:** Runs on Port `3000`. It serves the user interface.
*   **Process Manager (PM2):** Both applications are managed by PM2. PM2 ensures that if an application crashes or the EC2 instance reboots, the applications are automatically restarted and kept alive.

### 3. CI/CD Pipeline Flow
1.  **Developer Push:** A developer pushes code changes to the respective GitHub repository (`flask-backend` or `express-frontend`).
2.  **Webhook Trigger:** GitHub sends a webhook payload to Jenkins (running on Port `8080`) to trigger the corresponding pipeline.
3.  **Jenkins Build:** Jenkins checks out the latest code from the repository.
4.  **Dependency Installation:** Jenkins runs `pip install -r requirements.txt` for Flask and `npm install` for Express.
5.  **Deployment:** Jenkins executes the deployment script, which tells PM2 to restart the specific application (`pm2 restart flask-app` or `pm2 restart express-app`).
6.  **User Access:** Users can then access the updated applications via the EC2 instance's Public IP on ports `5000` and `3000`.
```