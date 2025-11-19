# KUGuide/management/commands/runserver_open.py
import webbrowser
import threading
import time
from django.core.management.commands.runserver import Command as RunserverCommand


class Command(RunserverCommand):
    help = 'Starts the development server and opens the browser'

    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument(
            '--no-browser',
            action='store_true',
            help='Do not open browser automatically',
        )

    def handle(self, *args, **options):
        # Get the address and port
        self.use_ipv6 = options.get('use_ipv6')
        if self.use_ipv6:
            self.addr = '::'
        else:
            self.addr = options.get('addrport', '')
            if not self.addr:
                self.addr = '127.0.0.1:8000'
        
        # Parse address and port
        if ':' in self.addr:
            addr, port = self.addr.rsplit(':', 1)
        else:
            addr = self.addr
            port = '8000'
        
        # Always use localhost for the browser
        url = f'http://localhost:{port}'
        
        # Open browser after a short delay (unless --no-browser is specified)
        if not options.get('no_browser'):
            def open_browser():
                time.sleep(1.5)  # Wait for server to start
                self.stdout.write(self.style.SUCCESS(f'\nOpening browser at {url}'))
                webbrowser.open(url)
            
            thread = threading.Thread(target=open_browser)
            thread.daemon = True
            thread.start()
        
        # Call the parent runserver command
        super().handle(*args, **options)