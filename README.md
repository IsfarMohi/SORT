# Object Tracking with YOLO and SORT

This project utilizes YOLO for object detection and SORT for object tracking in video streams. The primary objective is to detect and track persons in the provided video.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/IsfarMohi/SORT.git
    cd SORT
    ```

2. **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

    Ensure your `requirements.txt` file includes:
    ```plaintext
    opencv-python
    pandas
    ultralytics
    cvzone
    numpy
    ```

3. **Download the YOLOv8 model:**
    Download the YOLOv8 model file (`yolov8s.pt`) and place it in the root directory of the project.

4. **Ensure video and class list files are available:**
    Make sure you have a video file named `p.mp4` and a class list file named `coco.txt` in the root directory.

## Usage

1. **Run the main script:**
    ```sh
    python main.py
    ```

2. **View the video with detections and tracking:**
    The video will be displayed with detected and tracked persons highlighted. Move your mouse over the video window to get the RGB coordinates.

3. **Exit the video window:**
    Press `ESC` to exit the video window.

## Technologies Used

- **OpenCV:** For video processing and display.
- **Pandas:** For data manipulation.
- **Ultralytics YOLO:** For object detection.
- **SORT:** For object tracking.
- **cvzone:** For easier OpenCV functionalities.
- **NumPy:** For numerical operations.

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the repository.**
2. **Create your feature branch:**
    ```sh
    git checkout -b feature/YourFeature
    ```
3. **Commit your changes:**
    ```sh
    git commit -m 'Add some feature'
    ```
4. **Push to the branch:**
    ```sh
    git push origin feature/YourFeature
    ```
5. **Open a pull request.**

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues, please open an issue on [GitHub](https://github.com/IsfarMohi/SORT/issues) or contact the project owner at [IsfarMohi](https://github.com/IsfarMohi).
