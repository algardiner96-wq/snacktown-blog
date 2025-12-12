# Snacktown Blog

> Playful diner-style blog built with Django and Bootstrap. Deployed to Heroku with Cloudinary-backed media and WhiteNoise for static files.

---

## Quick Links
- [Live site](https://your-live-url.example.com) 
- [GitHub repo](https://github.com/algardiner96-wq/snacktown-blog)

---

<details>
<summary><strong>Introduction</strong></summary>

![Snacktown Introduction](docs/images/introduction.png)

Snacktown Blog is a satirical blog web application built for my Full Stack individual Capstone project which marks everything learnt at the Code Institute. Snacktown implements:

- **Frontend Development**: HTML, CSS, JavaScript
- **Backend Development**: Python, Django framework
- **Database Management**: PostgreSQL, integrated through Django ORM
- **API**: Cloudinary
- **AI Integration**: Purely for the images
- **Agile Methodology**: Project planning and tracking using Agile principles
- **Version Control**: Git & GitHub
- **Deployment**: Heroku

</details>

<details>
<summary><strong>UX Design</strong></summary>

- Goals: To create a fun user-friendly platform with over the top humour, strange menu items and interesting characters 
- Visual language: checkerboard background, bold primary red, mayo/green accents, comic-style headings.
- Accessibility: strong color contrast, focus styles via Bootstrap, semantic HTML sections.

</details>

<details>
<summary><strong>Features</strong></summary>

- Menu carousel and cards with aspect-ratio-safe images.
- Blog grid with lazy-loaded thumbnails.
- Recent reviews section.
- About banner featuring mascot preload for lower LCP.
- Responsive navbar with collapse on small screens.
- Comedic articles with related imagery 
- Premade joke comments

</details>

<details>
<summary><strong>User Stories</strong></summary>

- **Story:** As an account holder, I can write a review for a menu item so that others can read it.
- **Acceptance:** Logged-in users can create reviews; each review requires a rating and a comment; the review is saved and displayed under the correct menu item.

- **Story:** As a user, I can register, log in, and log out so that I can have an account.
- **Acceptance:** Users can create an account via the registration form; invalid credentials show an error message.

- **Story:** As a reviewer, I can edit or delete my review so that it can be updated or removed.
- **Acceptance:** Logged-in users can edit or delete their reviews; a message "Are you sure?" is displayed before deletion; a confirmation message is shown.

- **Story:** As a site user, I can filter the reviews by menu item so that I can read specific reviews.
- **Acceptance:** Reviews can be filtered by selecting a menu item; only reviews for the selected item are displayed; if no reviews exist for an item, a "No reviews yet" message appears.

- **Story:** As a site admin, I can manage menu items so that I can change what is available.
- **Acceptance:** Admin can add, edit, and delete menu items; menu items display correctly on the menu list page with name, image, and description; deleted items no longer appear.

- **Story:** As a site visitor, I can read blog posts so that I can see the satirical posts.
- **Acceptance:** Blog index lists all posts with title, date, and image; clicking a post displays the full content.

- **Story:** As a site admin, I can create, edit, and delete blog posts so that I can manage Snacktown's content.
- **Acceptance:** Admin can add, edit, and delete blog posts via front-end forms; blog posts update immediately after changes; deleted posts no longer appear.

- **Story:** As a Snacktown fan, I can see images of menu items and satirical posts so that I can enjoy the content.
- **Acceptance:** Menu images display correctly; satirical images load without errors.

- **Story:** As a site visitor, I can experience blog posts with Snacktown's distinctive font, colour palette, and whimsical mascot so that the site feels more playful.
- **Acceptance:** The colour palette and font are consistently applied across headings, links, and backgrounds; Snacktown's playful identity is visible via mascot or themed decorative elements.

</details>

<details>
<summary><strong>Font</strong></summary>

- Headings: Bangers (display)
- Body: Rubik, Arial fallback

</details>

<details>
<summary><strong>Colour Palette</strong></summary>

| Token | Value | Usage |
| --- | --- | --- |
| `--primary` | `#FF3B3F` | Accents, headings, borders |
| `--secondary` | `#A4DE02` | Hover, secondary CTAs |
| `--accent` | `#F5D7A1` | Navbar, footer background |
| `--background` | `#2E2E2E` | Dark surfaces |
| `--text` | `#FDFDFD` | Main text on dark bg |
| `--dark-accent` | `#1a1a1a` | Cards, panels |

Palette snapshot: ![Snacktown Colour Palette](docs/images/Snacktown%20colour%20pallete.jpg)

</details>

<details>
<summary><strong>Images</strong></summary>

- Media hosted on Cloudinary (production); local dev uses Django file storage.
- Hero/mascot: preloaded with `fetchpriority="high"` for faster LCP.
- Thumbnails: `loading="lazy"` and constrained with `aspect-ratio` to prevent CLS.

Screenshots:
- ![Home hero](docs/images/hero.png)
- ![Menu carousel](docs/images/menu%20carousel.png)
- ![Blog grid](docs/images/blog%20posts.png)

</details>

<details>
<summary><strong>Wireframes</strong></summary>

- Desktop: ![Snacktown Wireframe (Desktop)](docs/wireframes/snacktown%20finshed%20wireframe.jpg)
- Mobile: ![Snacktown Wireframe (Mobile)](docs/wireframes/mobile%20wireframe.png)

</details>

<details>
<summary><strong>Responsiveness</strong></summary>

- Mobile-first breakpoints at 991px and 575px for nav, carousel, grids.
- Enforced `aspect-ratio` on menu/blog images; capped heights on mobile.
- Overflow guards on body/container to avoid horizontal scroll.

</details>

<details>
<summary><strong>Agile</strong></summary>

- **Board:** [GitHub Project Board](https://github.com/users/algardiner96-wq/projects/8)
- **Workflow:** Kanban-style board (To Do → In Progress → Done).
- **Methodology:** MoSCoW prioritization applied to user stories:
  - **Must Have:** Core features (auth, blog, menu, reviews)
  - **Should Have:** Enhanced UX (theme, search, pagination)
  - **Could Have:** Future enhancements (RSS, tags, dark mode)
  - **Won't Have:** Out of scope items
- **Iterations:** Focused on deploy stability, mobile UX, and performance (CLS/LCP).
- **Peer Review:** Commits reviewed before deploy to Heroku.

</details>

<details>
<summary><strong>ERD</strong></summary>

- Diagram: ![Snacktown ERD](docs/testing/Snacktown%20ERD.png)

</details>

<details>
<summary><strong>Issues</strong></summary>

- Resolved: CSS parse error after media query; fixed by removing stray token.
- Resolved: Heroku 500s due to empty DATABASE_URL; added guard fallback to SQLite.
- Resolved: Static files missing; configured WhiteNoise and collectstatic.
- Resolved: Media loading; secured Cloudinary settings.

A big issue was accidently uploading my env.py, so i had to change database and update my secret credentials to protect my project. I deleted all the logs and restarted the project on 08/12/2025 to avoid any missing logs.



</details>

<details>
<summary><strong>Lighthouse & Testing</strong></summary>

- Latest Lighthouse run: see [docs/testing/lighthouse.png](docs/testing/lighthouse.png) (replace if you capture separate desktop/mobile reports).
- Coverage: home page focus (CLS/LCP); follow-up runs recommended after image swaps.
- Plan: add responsiveness screenshots and any manual test notes under `docs/testing/`.

</details>

<details>
<summary><strong>Future Features</strong></summary>

- User auth for comments/reviews with moderation.
- Search and pagination for blog posts and menu items.
- Tags/categories for posts and menu filtering.
- Dark/light theme toggle that respects user preference.
- RSS feed and sitemap for better SEO and content discovery.
- Compress images for faster loading.

</details>

<details>
<summary><strong>AI Implementation</strong></summary>

- GPT-5.1-Codex-Max (Preview) assisted with refactoring, performance tuning, and documentation drafting.
- Prompts focused on CLS/LCP mitigation, responsive CSS, and deployment fixes.
- All the imaages and logo were created by various Ai generators.

</details>

<details>
<summary><strong>Deployment</strong></summary>

- Platform: Heroku (Gunicorn + Django 4.2, Python 3.12).
- Static files: WhiteNoise; run `python manage.py collectstatic` during release.
- Media: Cloudinary (set `CLOUDINARY_URL`).
- Database: Postgres via `DATABASE_URL`; fallback to SQLite locally when unset.
- Key env vars: `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, `DATABASE_URL`, `CLOUDINARY_URL`.
- Typical release steps:
  1) `pip install -r requirements.txt`
  2) `python manage.py migrate`
  3) `python manage.py collectstatic --noinput`
  4) `git push heroku main` (or via CI/CD)

</details>
