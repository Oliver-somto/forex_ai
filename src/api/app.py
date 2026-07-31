from fastapi import FastAPI

app = FastAPI(title='Project Oracle API', version='0.1.0')

@app.get('/')
def root():
    return {'status': 'ok', 'message': 'Project Oracle is alive'}

@app.get('/health')
def health_check():
    return {'status': 'healthy'}