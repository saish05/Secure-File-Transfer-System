# Secure-File-Transfer-System

**Description:**
The Secure Multi-Client File Transfer System is a Python-based application designed to facilitate secure file transfers between multiple clients over a network. This system ensures end-to-end encryption and employs socket programming techniques for establishing connections between clients and a central server. All file transfer operations are regulated by the server, enhancing security and control over data transmission. The system supports the exchange of various file formats including MS Word documents, PDFs, images, videos, and more. Users can effortlessly send and receive files, with each client's interactions managed centrally by the server.

As a demonstration, I have shown with two clients where client2 sends test files to client1, and client1 receives and saves the files with designated names.

**Features:**
1. **Centralized Control:** All file transfer operations are regulated by the server, providing centralized control and enhancing security.
2. **Multi-Client Support:** Supports multiple clients concurrently, enabling seamless file transfers between any number of connected clients.
3. **File Format Agnosticism:** Facilitates the transfer of diverse file formats, ensuring compatibility with MS Word documents, PDFs, images, videos, and other document formats.
4. **End-to-End Encryption:** Implements secure socket programming techniques to establish encrypted connections between clients, ensuring data confidentiality during transmission.
5. **Scalability:** Easily scalable to accommodate additional clients and handle larger file transfers, making it suitable for networks of varying sizes.
6. **Robust Error Handling:** Incorporates robust error handling mechanisms to address connection issues and ensure reliable data transmission across the network.
7. **User-Friendly Interface:** Provides a simple and intuitive interface for clients to send and receive files, enhancing user experience and usability.
8. **Cross-Platform Compatibility:** Compatible with various operating systems, ensuring flexibility and accessibility across different environments.

**Repository Structure:**
- **client.py:** Contains the client-side code for initiating file transfers and receiving files, with all functions regulated by the server.
- **server.py:** Includes the server-side code for managing client connections, handling file transfer requests, and ensuring centralized control over the system.
- **README.md:** Provides comprehensive instructions on setting up and running the Secure Multi-Client File Transfer System, along with usage guidelines and configuration options.


**Usage:**
1. Clone the repository to your local machine.
2. Run the server script (`server.py`) on a designated host.
3. Execute the client script (`client.py`) on each client machine.
4. Follow the prompts on the client-side interface to interact with the server and send/receive files securely.


