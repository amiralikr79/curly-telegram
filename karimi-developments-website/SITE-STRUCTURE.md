# SITE STRUCTURE & NAVIGATION — Karimi Developments

---

## Document Overview

This document outlines the complete website structure, navigation hierarchy, internal linking strategy, and user flow for the Karimi Developments website.

**Purpose:** Provide clear blueprint for site architecture and navigation implementation  
**Last Updated:** December 2025  
**Status:** Final and ready for implementation

---

## Site Architecture Overview

**Site Type:** Multi-page business website  
**Total Pages:** 8 primary pages + footer/utility pages  
**Navigation Style:** Horizontal top navigation with optional mobile hamburger menu  
**Structure:** Flat hierarchy with clear parent-child relationships

---

## Primary Navigation Structure

### Desktop Navigation Bar

**Logo/Wordmark (Left):**
- Karimi Developments
- Links to: Homepage (/)
- Always visible, sticky header recommended

**Main Navigation Items (Right):**

```
About  |  Philosophy  |  Our Approach  |  Portfolio  |  Pipeline  |  Investors  |  Contact
```

**Full Navigation Breakdown:**

1. **About** → `/about`
2. **Philosophy** → `/philosophy`
3. **Our Approach** → `/our-approach`
4. **Portfolio** → `/portfolio`
5. **Pipeline** → `/pipeline-strategy`
6. **Investors** → `/investor-relations`
7. **Contact** → `/contact`

**Note:** "Home" is implicit (logo click returns to home). Keep navigation clean and minimal.

---

### Mobile Navigation (< 768px)

**Mobile Header:**
- Logo: Left-aligned
- Hamburger Menu Icon: Right-aligned (three horizontal lines)

**Mobile Menu Drawer:**
- Slide-in from right or expand from top
- Full-screen or overlay style
- Same navigation items as desktop, stacked vertically
- Larger touch targets (minimum 48px height)
- Close button (X) visible in top-right corner

**Mobile Menu Order:**
1. About
2. Philosophy
3. Our Approach
4. Portfolio
5. Pipeline Strategy
6. Investor Relations
7. Contact

Optional: Add visual divider between "Pipeline Strategy" and "Investor Relations" to separate public vs. investor-focused content.

---

## Page Hierarchy & Relationships

### Tier 1: Core Brand Pages (Public-Facing)

**Homepage** (`/`)
- Primary entry point
- Links to: All pages
- Featured: Portfolio preview, Philosophy preview
- Primary CTAs: "Explore Our Work" (Portfolio), "Our Philosophy" (Philosophy)

**About** (`/about`)
- Who we are, values, team, story
- Links to: Philosophy, Our Approach, Contact
- Primary CTA: "Get in Touch" (Contact), "View Our Approach" (Our Approach)

**Philosophy** (`/philosophy`)
- Design manifesto, principles
- Links to: Our Approach, Portfolio, About
- Primary CTA: "See How We Work" (Our Approach), "View Our Projects" (Portfolio)

**Our Approach** (`/our-approach`)
- Development process, methodology
- Links to: Portfolio, Investor Relations, Contact
- Primary CTA: "Contact Us" (Contact), "Investor Information" (Investor Relations)

**Portfolio** (`/portfolio`)
- Conceptual projects showcase
- Links to: Philosophy, Our Approach, Contact
- Primary CTA: "Learn About Our Approach" (Our Approach), "Contact Us" (Contact)
- Internal anchors: #willow-house, #ridgeview, #larch-residences

---

### Tier 2: Strategic & Investor Pages

**Pipeline Strategy** (`/pipeline-strategy`)
- 5-year strategic plan, markets, typologies
- Links to: Investor Relations, Our Approach, Contact
- Primary CTA: "Investor Information" (Investor Relations)

**Investor Relations** (`/investor-relations`)
- Investment structures, returns, governance
- Links to: Pipeline Strategy, Our Approach, Contact
- Primary CTA: "Request Investor Information Pack" (Contact form or direct email)

---

### Tier 3: Utility Pages

**Contact** (`/contact`)
- Contact form, inquiry submission
- Links to: All pages (via "Related Pages" section)
- Primary CTA: "Send Message" (form submit)

---

## Footer Structure

### Footer Layout (Four Columns)

**Column 1: Brand**
- Logo/Wordmark: Karimi Developments
- Tagline: "Design. Discipline. Legacy."
- Optional: Brief one-line descriptor

**Column 2: Explore**
- About
- Philosophy
- Our Approach
- Portfolio
- Pipeline Strategy

**Column 3: Connect**
- Investor Relations
- Contact
- Landowner Inquiries

**Column 4: Contact Info**
- Email: hello@karimidevelopments.com
- Investor Email: investors@karimidevelopments.com
- Location: Metro Vancouver, BC

**Bottom Bar:**
- Left: © 2025 Karimi Developments. All rights reserved.
- Right: Privacy Policy | Terms of Use

**Social Media Icons (Optional):**
- If included: LinkedIn, Instagram (architectural/project-focused)
- Place in Column 4 or bottom bar center
- Only include if actively maintained

---

## Internal Linking Strategy

### Cross-Page Link Recommendations

**From Homepage:**
- Philosophy (via Philosophy preview section)
- Portfolio (via Portfolio preview cards)
- About (via "Who We Are" section)
- Contact (via final CTA section)

**From About:**
- Philosophy (via "Philosophy Bridge" section)
- Our Approach (via closing CTA)
- Contact (via closing CTA)

**From Philosophy:**
- Our Approach (via closing CTA: "See How We Work")
- Portfolio (via closing CTA: "View Our Projects")

**From Our Approach:**
- Portfolio (contextual mention of projects)
- Investor Relations (via "Risk Management" or closing CTA)
- Contact (via closing CTA)

**From Portfolio:**
- Philosophy (intro section: "principles they embody")
- Our Approach (closing CTA: "Learn About Our Approach")
- Contact (closing CTA)

**From Pipeline Strategy:**
- Investor Relations (closing CTA: "Investor Information")
- Our Approach (contextual link in "Development Typologies")

**From Investor Relations:**
- Pipeline Strategy (contextual link in investment structure)
- Our Approach (contextual mention of process)
- Contact (primary CTA: "Request Information Pack")

**From Contact:**
- Philosophy, Portfolio, Investor Relations (via "Related Pages" section)

---

## User Flow Scenarios

### Scenario 1: General Public / Prospective Homebuyer

**Entry:** Homepage  
**Journey:**  
1. Homepage → reads intro, views portfolio preview
2. Portfolio → explores conceptual projects
3. Philosophy → learns about design principles
4. About → understands company story
5. Contact → submits general inquiry

**Key Pages:** Home → Portfolio → Philosophy → About → Contact

---

### Scenario 2: Potential Investor

**Entry:** Homepage or direct to Investor Relations (via Google search)  
**Journey:**  
1. Investor Relations → reviews investment structure
2. Pipeline Strategy → evaluates growth plan
3. Our Approach → assesses operational capabilities
4. Portfolio → reviews design quality
5. Contact → requests investor information pack

**Key Pages:** Investor Relations → Pipeline → Our Approach → Portfolio → Contact

---

### Scenario 3: Landowner Seeking Partnership

**Entry:** Homepage or Contact (via Google search)  
**Journey:**  
1. Homepage → understands firm positioning
2. About → learns about values and approach
3. Our Approach → reviews development process
4. Contact → submits landowner inquiry (sites@karimidevelopments.com)

**Key Pages:** Home → About → Our Approach → Contact

---

### Scenario 4: Industry Professional / Architect / Consultant

**Entry:** Portfolio or Philosophy (via referral or social media)  
**Journey:**  
1. Portfolio → studies design work
2. Philosophy → reads design manifesto
3. Our Approach → reviews development process
4. About → understands firm culture
5. Contact → reaches out for collaboration

**Key Pages:** Portfolio → Philosophy → Our Approach → About → Contact

---

## Navigation Best Practices

### UX Guidelines

**Sticky Header:**
- Keep navigation visible during scroll
- Reduce height slightly after initial scroll (from 100px to 80px)
- Maintain logo and navigation items visible at all times

**Active State:**
- Highlight current page in navigation (underline or bold)
- Color: Muted Gold or slightly darker Charcoal
- Clear visual indicator of location

**Hover States:**
- Underline animation (slide in from left, 250ms)
- Or color shift to Muted Gold
- Smooth transition, 200ms duration

**Mobile Menu:**
- Smooth slide-in animation (300ms)
- Semi-transparent overlay behind menu (Charcoal, 50% opacity)
- Tap overlay to close menu
- No scrolling of main content when menu is open

**Breadcrumbs:**
- Not necessary for flat 8-page structure
- Consider only if adding sub-pages in future (e.g., individual project detail pages)

---

## URL Structure

### Clean URL Convention

**Format:** `karimidevelopments.com/[page-name]`

**All URLs:**
- `/` (Homepage)
- `/about`
- `/philosophy`
- `/our-approach`
- `/portfolio`
- `/pipeline-strategy`
- `/investor-relations`
- `/contact`

**Utility Pages:**
- `/privacy-policy`
- `/terms-of-use`

**NO trailing slashes preferred** (configure via server settings)

**URL Best Practices:**
- Use lowercase only
- Use hyphens (not underscores) for multi-word pages
- Keep URLs short and semantic
- Avoid numbers or dates in URLs
- Use canonical tags to prevent duplicate content

---

## SEO & Meta Structure

### Page Title Format

**Homepage:**
```
Karimi Developments — Boutique Infill Development in Metro Vancouver
```

**Other Pages:**
```
[Page Name] — Karimi Developments
```

Examples:
- `About — Karimi Developments`
- `Philosophy — Karimi Developments | Design, Discipline, Legacy`
- `Portfolio — Conceptual Projects | Karimi Developments`

**Length:** Keep under 60 characters (includes separators)

---

### Meta Description Format

**Length:** 150-160 characters (optimal for Google SERP display)  
**Structure:** Action-oriented, includes key terms, clear value proposition

**See individual page files for specific meta descriptions.**

---

### Structured Data (Schema.org)

**Recommended Schema Types:**

**Organization Schema (Homepage):**
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Karimi Developments",
  "url": "https://karimidevelopments.com",
  "logo": "https://karimidevelopments.com/logo.png",
  "description": "Boutique infill development in Metro Vancouver",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Metro Vancouver",
    "addressRegion": "BC",
    "addressCountry": "CA"
  }
}
```

**Real Estate Business Schema:**
```json
{
  "@context": "https://schema.org",
  "@type": "RealEstateAgent",
  "name": "Karimi Developments"
}
```

---

## Site Search (Optional)

**Recommendation:** Not necessary for 8-page site initially

**If adding later:**
- Use lightweight search solution (Algolia, Lunr.js, or platform-native)
- Place search icon in top navigation (right side, before Contact)
- Search scope: All pages, headings, and key copy
- Display: Overlay modal with instant results

---

## Analytics & Tracking

### Key Pages to Track

**Goal Completions:**
1. Contact form submission
2. Investor information request (button click)
3. Portfolio project views (time on page, scroll depth)
4. Pipeline Strategy page views (investor intent signal)
5. Email link clicks (hello@, investors@, sites@)

**Recommended Events:**
- CTA button clicks (track by button text)
- External link clicks (if any)
- PDF downloads (if investor pack available)
- Scroll depth on Philosophy page (engagement metric)
- Time on site by user segment (infer from entry page)

**Tools:**
- Google Analytics 4 (GA4)
- Optional: Hotjar or similar for heatmaps (Portfolio, Home, Investor pages)

---

## Accessibility (WCAG 2.1 AA Compliance)

### Navigation Accessibility Requirements

**Keyboard Navigation:**
- All navigation items must be keyboard accessible (Tab key)
- Visible focus indicators (outline or underline)
- Logical tab order (left to right, top to bottom)
- Escape key closes mobile menu

**Screen Reader Support:**
- Proper semantic HTML (`<nav>`, `<header>`, `<main>`, `<footer>`)
- ARIA labels where needed (e.g., "Main navigation", "Close menu")
- Skip to main content link (hidden but keyboard accessible)

**Color Contrast:**
- Navigation text: minimum 4.5:1 contrast ratio
- Use Charcoal (#2B2B2B) on Off-White (#FAFAF8): 13.8:1 ✓
- Use Cream (#F4F1EA) on Soft Black (#1A1A1A): 12.6:1 ✓

**Touch Targets (Mobile):**
- Minimum 48px × 48px touch target size
- Adequate spacing between navigation items (16px minimum)

---

## Performance Optimization

### Navigation Loading

**Above-the-Fold Priority:**
- Inline critical CSS for header/navigation
- Preload logo and navigation fonts
- Defer non-critical JavaScript

**Lazy Loading:**
- Not applicable to navigation (always load immediately)

**Asset Optimization:**
- Logo: SVG format (scalable, small file size)
- Icons: SVG or icon font
- Navigation background: Solid color (no image needed)

**Target Metrics:**
- Navigation visible in < 1 second
- Navigation interactive (clickable) in < 1.5 seconds

---

## Edge Cases & Considerations

### 404 Error Page

**Content:**
- Headline: "Page not found."
- Subheadline: "The page you're looking for doesn't exist or has been moved."
- CTA: "Return to Homepage" (button linking to /)
- Secondary Links: About, Portfolio, Contact

**Design:**
- Match site design language (Cream background, Charcoal text)
- Maintain header/footer navigation
- Keep minimal and helpful

---

### Maintenance Mode Page

**Use Case:** Site updates, scheduled maintenance

**Content:**
- Headline: "We'll be back shortly."
- Message: "Karimi Developments is currently undergoing scheduled maintenance."
- Contact: "For urgent inquiries: hello@karimidevelopments.com"
- Design: Minimal, centered layout, logo visible

---

## Future Expansion Considerations

### Potential Future Pages (Not Included in V1)

**Blog / Insights:**
- URL: `/insights`
- Purpose: Thought leadership, market commentary, project updates
- Navigation: Add to main nav or footer

**Press / Media:**
- URL: `/press`
- Purpose: Press releases, media coverage, press kit
- Navigation: Footer only (not main nav)

**Careers:**
- URL: `/careers`
- Purpose: Job listings, team culture
- Navigation: Footer only

**Individual Project Detail Pages:**
- URL: `/portfolio/[project-slug]`
- Example: `/portfolio/willow-house`
- Navigation: Accessed via Portfolio page, not main nav
- Structure: Sub-pages under Portfolio parent

**If adding sub-pages, update navigation to include dropdown menus.**

---

## Content Update Cadence

### Pages Requiring Regular Updates

**Never/Rarely:**
- Philosophy (timeless content)
- About (update only for major company changes)

**Annually:**
- Pipeline Strategy (update for new 5-year outlook)
- Investor Relations (update for new investment structures or performance data)

**Per-Project Basis:**
- Portfolio (add new conceptual projects as firm evolves)
- Homepage (refresh portfolio preview as new projects added)

**Ongoing:**
- Contact (ensure email addresses and inquiry types remain current)

---

## Version Control & Change Log

**Current Version:** 1.0 (December 2025)

**Change Log:**
- v1.0 (Dec 2025): Initial site structure, 8 primary pages
- Future updates: Document here

---

## Implementation Checklist

Before launch, verify:

- [ ] All 8 primary pages are published and accessible
- [ ] Navigation works on desktop and mobile
- [ ] All internal links are functional (no 404s)
- [ ] CTAs on every page link to correct destinations
- [ ] Footer is consistent across all pages
- [ ] Contact form is functional and sends emails correctly
- [ ] Meta titles and descriptions are set for all pages
- [ ] Logo links to homepage from every page
- [ ] Active navigation state works correctly
- [ ] Mobile menu opens/closes smoothly
- [ ] All pages pass WCAG AA contrast checks
- [ ] Site loads in under 3 seconds on average connection
- [ ] Analytics tracking is installed and verified
- [ ] 404 page is configured

---

**Document Status:** Complete  
**Last Updated:** December 2025  
**Approved For:** Implementation
