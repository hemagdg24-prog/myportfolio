// ══════════════════════════════════════════════════════════════════════════════
//  HEMAASWINI PERICHARLA — PORTFOLIO MAIN JS
// ══════════════════════════════════════════════════════════════════════════════

'use strict';

/* ── Navbar scroll effect ──────────────────────────────────────────────── */
(function initNavbar() {
    const navbar = document.getElementById('navbar');
    if (!navbar) return;

    window.addEventListener('scroll', () => {
        navbar.classList.toggle('scrolled', window.scrollY > 30);
    }, { passive: true });
})();

/* ── Mobile nav toggle ──────────────────────────────────────────────────── */
(function initMobileNav() {
    const toggle = document.getElementById('navToggle');
    const links  = document.getElementById('navLinks');
    if (!toggle || !links) return;

    toggle.addEventListener('click', () => {
        const open = links.classList.toggle('open');
        toggle.setAttribute('aria-expanded', open);
        document.body.style.overflow = open ? 'hidden' : '';
    });

    // Close on link click
    links.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => {
            links.classList.remove('open');
            toggle.setAttribute('aria-expanded', 'false');
            document.body.style.overflow = '';
        });
    });
})();

/* ── Reveal on scroll ───────────────────────────────────────────────────── */
(function initReveal() {
    const targets = document.querySelectorAll('.reveal-on-scroll');
    if (!targets.length) return;

    const observer = new IntersectionObserver(entries => {
        entries.forEach((entry, i) => {
            if (entry.isIntersecting) {
                // Staggered delay for grid items
                const siblings = [...entry.target.parentElement.children].filter(el => el.classList.contains('reveal-on-scroll'));
                const idx = siblings.indexOf(entry.target);
                setTimeout(() => {
                    entry.target.classList.add('revealed');
                }, idx * 60);
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.02, rootMargin: '60px 0px 60px 0px' });

    targets.forEach(el => observer.observe(el));

    // Fallback: reveal all targets after 600ms so nothing stays blank if observer is bypassed
    setTimeout(() => {
        targets.forEach(el => el.classList.add('revealed'));
    }, 600);
})();

/* ── Animated background particles ─────────────────────────────────────── */
(function initParticles() {
    const container = document.getElementById('bgParticles');
    if (!container) return;

    for (let i = 0; i < 18; i++) {
        const dot = document.createElement('div');
        dot.style.cssText = `
            position: absolute;
            width: ${Math.random() * 3 + 1}px;
            height: ${Math.random() * 3 + 1}px;
            background: ${Math.random() > 0.5 ? 'rgba(139,92,246,' : 'rgba(99,230,252,'}${(Math.random() * 0.4 + 0.1).toFixed(2)})`;
            border-radius: 50%;
            left: ${Math.random() * 100}%;
            top: ${Math.random() * 100}%;
            animation: float-particle ${6 + Math.random() * 8}s ease-in-out infinite;
            animation-delay: ${Math.random() * 5}s;
        `;
        container.appendChild(dot);
    }

    // Inject keyframes
    if (!document.getElementById('particle-style')) {
        const style = document.createElement('style');
        style.id = 'particle-style';
        style.textContent = `
            @keyframes float-particle {
                0%, 100% { transform: translate(0, 0) scale(1); opacity: .6; }
                33%       { transform: translate(${Math.random() * 30 - 15}px, ${Math.random() * 30 - 15}px) scale(1.3); opacity: 1; }
                66%       { transform: translate(${Math.random() * 20 - 10}px, ${Math.random() * 20 - 10}px) scale(.8); opacity: .4; }
            }
        `;
        document.head.appendChild(style);
    }
})();

/* ── Smooth hover glow on cards ─────────────────────────────────────────── */
(function initCardGlow() {
    document.querySelectorAll('.project-card, .achievement-card, .skill-category-card').forEach(card => {
        card.addEventListener('mousemove', e => {
            const rect = card.getBoundingClientRect();
            const x = ((e.clientX - rect.left) / rect.width) * 100;
            const y = ((e.clientY - rect.top)  / rect.height) * 100;
            card.style.setProperty('--mouse-x', x + '%');
            card.style.setProperty('--mouse-y', y + '%');
        });
    });
})();

/* ── Page load fade ─────────────────────────────────────────────────────── */
(function initPageLoad() {
    document.body.style.opacity = '0';
    document.body.style.transition = 'opacity .5s ease';
    window.addEventListener('load', () => {
        document.body.style.opacity = '1';
    });
})();

/* ── Active nav link highlight based on scroll (home only) ─────────────── */
(function initScrollSpy() {
    const sections = document.querySelectorAll('section[id]');
    if (!sections.length) return;

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
                const link = document.querySelector(`.nav-link[href="#${entry.target.id}"]`);
                if (link) link.classList.add('active');
            }
        });
    }, { threshold: 0.5 });

    sections.forEach(s => observer.observe(s));
})();
