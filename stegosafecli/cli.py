"""
StegoSafeCLI - Command-line tool for LSB steganography with optional AES encryption.
"""
import argparse
from stegosafecli.stego import hide_message, reveal_message
from stegosafecli.crypto import encrypt_message, decrypt_message
from stegosafecli.log import log_operation
import sys


def main():
    parser = argparse.ArgumentParser(description='StegoSafeCLI: Hide or reveal messages in images using LSB steganography.')
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Hide command
    hide_parser = subparsers.add_parser('hide', help='Hide a message in an image')
    hide_parser.add_argument('-i', '--input', required=True, help='Input image path')
    hide_parser.add_argument('-o', '--output', required=True, help='Output image path')
    hide_parser.add_argument('-m', '--message', help='Message to hide')
    hide_parser.add_argument('--message-file', help='Path to file containing message')
    hide_parser.add_argument('--encrypt', choices=['AES-128', 'AES-256'], help='Encrypt message before hiding')
    hide_parser.add_argument('--key', help='Encryption key (required if --encrypt is used)')

    # Reveal command
    reveal_parser = subparsers.add_parser('reveal', help='Reveal a hidden message from an image')
    reveal_parser.add_argument('-i','--input', help='Path to stego image')
    reveal_parser.add_argument('--decrypt', choices=['AES-128', 'AES-256'], help='Decrypt message after revealing')
    reveal_parser.add_argument('--key', help='Decryption key (required if --decrypt is used)')

    args = parser.parse_args()

    if args.command == 'hide':
        if not args.message and not args.message_file:
            print('Error: Provide --message or --message-file')
            sys.exit(1)
        if args.message_file:
            with open(args.message_file, 'r', encoding='utf-8') as f:
                message = f.read()
        else:
            message = args.message
        if args.encrypt:
            if not args.key:
                print('Error: --key is required for encryption')
                sys.exit(1)
            message = encrypt_message(message, args.key, args.encrypt)
            mode = f'LSB+{args.encrypt}'
        else:
            mode = 'LSB'
        hide_message(args.input, args.output, message)
        log_operation('hide', args.input, args.output, mode)
        print(f'Message hidden in {args.output}')

    elif args.command == 'reveal':
        message = reveal_message(args.input)
        mode = 'LSB'
        if args.decrypt:
            if not args.key:
                print('Error: --key is required for decryption')
                sys.exit(1)
            message = decrypt_message(message, args.key, args.decrypt)
            mode = f'LSB+{args.decrypt}'
        log_operation('reveal', args.input, None, mode)
        print('Hidden message:')
        print(message)

if __name__ == '__main__':
    main()
