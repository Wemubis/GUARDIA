# Projet-4-RFID

### Circuit design and documentation:

#### 1) ESP8266 Module (NodeMCU):

This module is used as the main microcontroller for the system. It integrates the ESP8266 WiFi module and offers a platform compatible with Arduino.

#### 2) RFID Module (MFRC522):

The MFRC522 RFID module is used for reading RFID cards. It communicates with the ESP8266 via SPI (Serial Peripheral Interface).

A second MFRC522 RFID module is used for writing to RFID cards. It communicates with the ESP32-C3, also via SPI (Serial Peripheral Interface).

#### 3) Raspberry Pi 4:

The Raspberry Pi 4 allows for an SQL database to which our ESP8266 module can connect to retrieve information about the cards, check if they are valid or not, and determine their access rights.

The communication between the database and the ESP8266 occurs via WiFi.

#### 4) Circuit Diagram:

![Circuit diagram](https://github.com/SebastienCherki/Projet-4-RFID/blob/main/dependencies/Schema_ESP32_RC522.png)

<br>

## Justification for technical and UX choices:

### 1) Use of libraries:

We integrated libraries such as **ESP8266WiFi.h**, **ESP8266HTTPClient.h**, **ArduinoJson.h**, and **MFRC522.h** in addition to the base libraries to simplify our work with the ESP8266, HTTP requests, JSON processing, and the RFID reader.

### 2) WiFi configuration:

WiFi connection information (SSID and password) is stored as constants (ssid and password) for better readability. However, it is recommended to adopt more secure methods to store such sensitive data.

### 3) Server URL:

The server URL is defined as a constant _(serverUrl)_, making it easier to modify in case of server changes. This makes our code more flexible.

### 4) HTTPS and WiFiClientSecure:

To secure data exchanges, we use the HTTPS protocol with _WiFiClientSecure_, ensuring encryption of data between the device and the server.

### 5) Serial communication:

Serial communication is integrated to facilitate debugging by displaying status messages on the serial monitor, helping to understand the flow of the program.

### 6) Code structure:

The code is organized into different core functions, such as _`setup()`_ and _`loop()`_, separating initialization and repetitive operations.

We added several other functions to improve the readability and understanding of the code:
- We have the _`addText()`_ & _`changeKeys()`_ functions in [write_key_text_card.ino](src/write_key_text_card.ino) that allow us to add text on 16 bytes and change keys in all sectors except sector 0, which remains in clear text (a choice made by the team).
- And we have the _`readCard()`_ & _`checkKeys()`_ functions in [Projet_RFID.ino](src/Projet_RFID.ino) that allow us to read the UID of the badges and verify authentication with the correct keys on the sectors where they have been modified.

### 7) Error handling:

Error checks are included, such as verifying the WiFi connection status, status after authentication or writing to the cards, and managing HTTP errors, ensuring the robustness of the program even in case of issues.

For each error, we retrieve the associated code, display everything on the serial output, and exit our conditions/loops to return to the starting point of the `void loop()` function.

We retrieved error codes using the following functions:
- _`mfrc522.GetStatusCodeName(status)`_ during authentication tests or when writing to the card.
- _`httpCode`_ for HTTP error codes.
- _`errer.c_str()`_ for parsing the JSON.

<br>

> [!NOTE]
> A delay of one second _`delay(1000)`_ between RFID card reads was added to avoid too frequent readings, allowing for customization based on specific needs.
