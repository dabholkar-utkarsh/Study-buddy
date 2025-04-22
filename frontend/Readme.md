# Study Buddy Frontend

This is the frontend application for Study Buddy, an intelligent learning assistant that helps students learn through natural conversations via text or voice interaction.

## Features

- Interactive landing page
- Conversational interface for learning
- Text-based Q&A
- Voice interaction support
- Support for various academic subjects
- Progress tracking

## Prerequisites

Before you begin, ensure you have the following installed:

- [Node.js](https://nodejs.org/) (v18.x or later recommended)
- [npm](https://www.npmjs.com/) (v9.x or later recommended)
- [Angular CLI](https://angular.io/cli) (v19.x)

## Installation

Follow these steps to set up the frontend application:

1. **Clone the repository** (if you haven't already):

   ```bash
   git clone https://github.com/yourusername/Study-buddy.git
   cd Study-buddy/frontend/StudyBuddy-ui
   ```

2. **Install dependencies**:

   ```bash
   npm install
   ```

   This will install all required packages defined in the `package.json` file.

## Running the Application

### Development Server

To start the development server:

```bash
npm start
```

Or alternatively:

```bash
ng serve
```

This will launch the application on `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

### Development Server with API Connection

If you need to connect to the backend API running on a different port:

```bash
ng serve --proxy-config proxy.conf.json
```

### Production Build

To build the application for production:

```bash
npm run build
```

Or:

```bash
ng build --configuration production
```

The build artifacts will be stored in the `dist/` directory.

## Project Structure

- `src/app/landing-page`: Landing page component
- `src/app/chat`: Chat interface for interacting with the Study Buddy
- `src/app/shared`: Shared components, services, and utilities
- `src/assets`: Static assets like icons and styles

## Working with the Backend

This frontend application communicates with a Flask backend. Make sure the backend server is running (typically on port 5000) before using features that require API communication.

To set up the backend, please refer to the README in the `backend/` directory.

## Testing

### Running Unit Tests

```bash
npm test
```

Or:

```bash
ng test
```

### Running End-to-End Tests

```bash
ng e2e
```

## Deployment

For deployment to production environments:

1. Build the application using the production configuration:

   ```bash
   ng build --configuration production
   ```

2. Deploy the contents of the `dist/` directory to your web server or hosting service.

## Troubleshooting

- **Missing dependencies**: Make sure you've run `npm install` successfully
- **Angular CLI not found**: Install it globally with `npm install -g @angular/cli`
- **Backend connection issues**: Verify that the backend server is running and accessible
- **Compilation errors**: Check console output for specific error messages

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.