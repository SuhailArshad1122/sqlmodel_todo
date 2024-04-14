import uvicorn


print('main function invoked')

if __name__ == '__main__':
    uvicorn.run('src.api:app', reload=True)