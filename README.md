
## Usage

### User Registration

- Navigate to the registration page: `/register/`.
- Fill out the form with a username, email, and password.
- Check your email to verify your account.

### User Login

- Navigate to the login page: `/login/`.
- Enter your credentials to access your account.

### Password Reset

- Navigate to the password reset page: `/password_reset/`.
- Enter your email to receive a reset link.

### Change Password

- Navigate to the change password page: `/change_password/`.
- Enter your current and new passwords to update your credentials.

## Customization

- **Templates**: Customize the HTML templates located in the `auth_system/templates/` directory.
- **Views**: Modify or extend the views in `auth_system/views.py` to fit your application's needs.
- **Forms**: Update the forms in `auth_system/forms.py` to add or remove fields.

## Testing

Run the tests using the following command:

```bash
python manage.py test
