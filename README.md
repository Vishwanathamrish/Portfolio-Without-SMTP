# Personal Portfolio Website

A modern, responsive personal portfolio website built with Flask and TailwindCSS, featuring a clean design with dark/light mode support.

## Features

- 🌓 Dark/Light mode toggle with system preference detection
- 📱 Fully responsive design with mobile-first approach
- 🚀 Fast and optimized performance with minimal dependencies
- 🎨 Modern UI powered by TailwindCSS
- 📄 Complete portfolio sections:
  - Home page
  - Projects showcase
  - Education timeline
  - About section
  - Contact information
- 🔗 Social media integration
- ⚡ Zero external CSS dependencies
- 🎨 Smooth transitions and animations
- 📱 Mobile-friendly navigation menu

## Tech Stack

- **Backend:** Flask (Python web framework)
- **Frontend:** 
  - HTML5 for structure
  - TailwindCSS for styling
  - Vanilla JavaScript for interactivity
  - 
  - Lucide Icons for UI elements
│   ├── images/       # Project and profile pictures
│   └── pdf/          # Resume and other documents
└── templates/         # HTML templates with inline TailwindCSS and JavaScript
    ├── about.html    # About page
    ├── contact.html  # Contact page with email form
    ├── education.html# Education page
    ├── home.html     # Home page
    └── project.html  # Projects page
```

Note: CSS and JavaScript are implemented inline in HTML files using TailwindCSS and vanilla JavaScript for optimal performance.

## Setup and Installation

1. Clone the repository
```bash
git clone <your-repo-url>
cd portfolio-site
```

2. Create a virtual environment and activate it
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the application
```bash
python app.py
```

The site will be available at `http://localhost:5000`

## Customization

1. **Content**: Update the HTML files in the `templates/` directory
2. **Styling**: Modify TailwindCSS classes directly in the HTML files
3. **Theme**: Default theme can be set to dark/light in the theme script
4. **Images**: Replace project and profile images in `static/images/`
5. **Resume**: Update your resume in `static/pdf/`
6. **Social Links**: Update your social media links in the contact section to make them accessible to visitors

## Features to Add

- [ ] Blog section
- [ ] Project filtering
- [ ] Skills progress bars
- [ ] Testimonials section
- [ ] Analytics integration

## Contributing

Feel free to fork this project and customize it for your own use. If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.


## Contact

Feel free to reach out to me for any questions or collaboration opportunities.

- Email: vishwanathamrish@gmail.com
- LinkedIn: https://www.linkedin.com/in/vishwanath-r-4a940721b
- GitHub: https://github.com/Vishwanathamrish

---

Made with ❤️ by Vishwanath.R
