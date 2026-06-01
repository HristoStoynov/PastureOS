# Deployment notes

Local development
- `docker-compose.yml` provides local Postgres, Redis, and backend API for development.

Cloud
- Recommend small AWS or GCP setup for pilots: managed Postgres (RDS/Cloud SQL), Redis (Elasticache/Memorystore), container host (ECS/GKE/Cloud Run) or Fly.io for simplicity.
- Use HTTPS, VPC/private subnets for DB.

CI
- GitHub Actions for lint, tests, and build artifacts.
