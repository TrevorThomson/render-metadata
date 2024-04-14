
'''
Run the database service locally
Usage:
    python database
'''

from render.service import create_service

if __name__ == '__main__':
    service = create_service()
    service.run()
