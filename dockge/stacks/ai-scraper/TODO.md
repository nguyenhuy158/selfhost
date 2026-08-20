# AI Scraper Tasks 🕷️

## Features Checklist
- [x] **Core Extraction Engine**: Powered by Gemini 2.0 Flash.
- [x] **Bilingual Support**: EN/VI toggle with `alpine-i18n`.
- [x] **Theme Management**: Manual toggle & Auto Dark Mode (18h-6h).
- [x] **Authentication**: Secure login with `huy/huy`.
- [x] **Data Persistence**: Integrated PostgreSQL for history and schedules.
- [x] **UI/UX**: AlpineJS logic, Toastify notifications, and Bottom Bar navigation.
- [x] **Modular Settings**: API Key and Model selection moved to dedicated tab.

## Future Enhancements
- [ ] **Background Worker**: Ensure the Python cron engine is processing scheduled tasks in the background.
- [ ] **Firecrawl Integration**: Use Firecrawl for better dynamic content handling.
- [ ] **Export Options**: Export PostgreSQL results to CSV/Excel.
- [ ] **Data Preview**: Inline viewer for saved JSON results in the History tab.

## Deployment
- [x] **Dockerized**: Multi-container setup (App + DB).
- [x] **Tunnel Ready**: Configured for `scraper.example.com`.
