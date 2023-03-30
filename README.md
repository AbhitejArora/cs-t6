# cs-t6

## Environment Setup

### Backend

```bash
cd server
python -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

### Frontend

```bash
cd client
yarn install # or `npm install`
```

## Execution

To run the backend, run `flask --app main run` from the `server` directory.

To run the frontend, run `yarn run dev` or `npm run dev` from the `client` directory.
