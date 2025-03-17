name: Deploy Python CLI App to EC2

on:
  workflow_dispatch

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Code
        uses: actions/checkout@v3  # Fetch latest code

      - name: Set up SSH Key
        run: |
          mkdir -p ~/.ssh
          echo "${{ secrets.EC2_SSH_KEY }}" > ~/.ssh/id_rsa
          chmod 600 ~/.ssh/id_rsa
          ssh-keyscan -H ${{ secrets.EC2_HOST }} >> ~/.ssh/known_hosts

      - name: Deploy to EC2
        run: |
          ssh ${{ secrets.EC2_USER }}@${{ secrets.EC2_HOST }} << 'EOF'
            # Navigate to app directory (or create if it doesn’t exist)
            mkdir -p ~/cli-app && cd ~/cli-app
            
            # Pull latest code
            git init
            git remote add origin https://github.com/riya-kochar19/Frontend.git || true
            git fetch origin main
            git reset --hard origin/main

            # Ensure Python is installed
            sudo apt update && sudo apt install -y python3 python3-pip

            # Install dependencies (if needed)
            if [ -f requirements.txt ]; then
              pip3 install -r requirements.txt
            fi

            # Make script executable (if it's a standalone CLI script)
            chmod +x app.py

            echo "Deployment successful!"
          EOF

