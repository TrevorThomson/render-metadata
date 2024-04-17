
'''
Run the render service locally
Usage:
    python renderer
'''

from render.service import create_service

if __name__ == '__main__':
    service = create_service(['localhost'])
    service.run()
