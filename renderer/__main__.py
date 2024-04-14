
'''
Run the Renderer service locally
Usage:
    python renderer
'''

from renderer.service import create_service

if __name__ == '__main__':
    service = create_service()
    service.run()
