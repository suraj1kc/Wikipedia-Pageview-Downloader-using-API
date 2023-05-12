# Wikipedia Pageview CSV Downloader

This Django project allows users to download pageview statistics from Wikipedia in CSV format. Users can provide a URL for the desired Wikipedia page, and the application will fetch the pageview data from the Wikipedia API and generate a CSV file for download.

## Folder Structure

- **wikidownloader**: Main project folder containing project-level settings and configurations.
- **downloader**: Django app folder containing the application logic and templates.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/suraj1kc/Wikipedia-Pageview-Downloader-using-API

2. Navigate to the project directory:

   ```shell
   cd wikidownloader

3. Install the required dependencies:
    ```shell
    pip install -r requirements.txt

4. Start the Django development server:
    ```shell
    python manage.py runserver

5. Access the application in your web browser at http://localhost:8000.

## Usage

1. Open the application in your web browser.
2. Paste the URL of the Wikipedia page for which you want to download the pageview statistics.
3. Click the "Download CSV" button.
4. The application will fetch the pageview data from the Wikipedia API and generate a CSV file.
5. The CSV file will be automatically downloaded to your local machine.

   E.g. https://en.wikipedia.org/wiki/Nepal
      
    ```shell
    https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/Nepal/daily/20001010/20220712

## Configuration

The project uses Django as the web application framework and Python for the backend logic. The following dependencies are required and are included in the `requirements.txt` file:

- Django==4.1.7
- pandas==1.5.2
- requests==2.28.1

## Contributing

Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). See the `LICENSE` file for details.

## Disclaimer

This project is intended for educational purposes only. The usage of the Wikipedia API is subject to the terms and conditions set by the Wikimedia Foundation. Please ensure that your usage of the application complies with the relevant API usage policies and guidelines.
