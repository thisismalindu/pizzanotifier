# Pizza Notifier

Pizza Notifier is a simple web application to store and manage your Pizza Hut Sri Lanka coupon codes. It helps you keep track of your coupons, their expiration dates, and notifies you about coupons that are about to expire.

## Features

- **Add Coupons**: Save your coupon codes with their expiration dates and type (15% or 20% discount).
- **Expiring Soon**: View a list of coupons that are going to expire within the next 3 days.
- **Manage Coupons**: View, edit, or delete your saved coupons. Delete coupons after using them if needed.
- **JSON Storage**: Coupons are stored in a `coupons.json` file for simplicity.
- **Easy Deployment**: Host this project on Vercel by forking the repository and connecting it to your Vercel account for automatic deployment.

## Requirements

- Python 3.x
- Flask

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/thisismalindu/pizzanotifier.git
    cd pizzanotifier
    ```

2. Install the required dependencies:
    ```bash
    pip install flask
    ```

3. Run the application:
    ```bash
    python app.py
    ```

4. Open your browser and navigate to `http://127.0.0.1:8080` or the configured port (Uncomment the last line if you are running this locally).

## Deployment on Vercel

1. Fork this repository to your GitHub account.
2. Connect the forked repository to your Vercel account.
3. Vercel will automatically deploy the application.

## File Structure

- `app.py`: Main Flask application file.
- `coupons.json`: JSON file to store coupon data.
- `templates/`: HTML templates for the web interface.
- `static/`: Static files (CSS, JS, etc.).

## Usage

1. Navigate to the "Add Coupon" page to save a new coupon.
2. View all your saved coupons on the "All Coupons" page.
3. Check the "Expiring Soon" section to see coupons expiring within 3 days.
4. Edit or delete coupons as needed.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

Enjoy your pizza while staying organized with Pizza Notifier! 🍕  
