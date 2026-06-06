/**
 * STEMAIDE Docs — Sidebar Navigation Enhancement
 * - Persists open/closed state of nav sections across page loads (localStorage)
 * - Smooth CSS-driven accordion transitions (handled via class toggling)
 * - Restores scroll position in the sidebar
 */
(function () {
  'use strict';

  var STORAGE_KEY = 'stemaide-nav-state';
  var SCROLL_KEY  = 'stemaide-nav-scroll';

  /* -----------------------------------------------------------------------
   * Helpers
   * --------------------------------------------------------------------- */
  function getState() {
    try { return JSON.parse(localStorage.getItem(STORAGE_KEY)) || {}; }
    catch (e) { return {}; }
  }

  function saveState(state) {
    try { localStorage.setItem(STORAGE_KEY, JSON.stringify(state)); }
    catch (e) {}
  }

  function getSidebarEl() {
    return document.querySelector('.md-sidebar--primary .md-sidebar__scrollwrap');
  }

  /* -----------------------------------------------------------------------
   * Collect all nav toggles (the <label> + <input type="checkbox"> pairs
   * that Material for MkDocs uses for collapsible sections)
   * --------------------------------------------------------------------- */
  function getNavToggles() {
    return Array.from(document.querySelectorAll(
      '.md-nav--primary .md-nav__toggle, ' +
      '.md-sidebar--primary .md-nav__toggle'
    ));
  }

  /* -----------------------------------------------------------------------
   * Restore persisted sidebar state
   * --------------------------------------------------------------------- */
  function restoreState() {
    var state = getState();
    if (!Object.keys(state).length) return;

    getNavToggles().forEach(function (toggle) {
      var id = toggle.id;
      if (!id) return;
      if (state[id] !== undefined) {
        toggle.checked = state[id];
      }
    });
  }

  /* -----------------------------------------------------------------------
   * Persist state on every toggle change
   * --------------------------------------------------------------------- */
  function persistOnChange() {
    getNavToggles().forEach(function (toggle) {
      toggle.addEventListener('change', function () {
        var state = getState();
        state[toggle.id] = toggle.checked;
        saveState(state);
      });
    });
  }

  /* -----------------------------------------------------------------------
   * Ensure the currently active page's ancestors are always expanded
   * --------------------------------------------------------------------- */
  function expandActiveAncestors() {
    var active = document.querySelector('.md-nav__item--active > .md-nav__toggle');
    if (active) { active.checked = true; }

    // Walk up the nav tree
    var el = document.querySelector('.md-nav__item--active');
    while (el) {
      var toggle = el.previousElementSibling;
      if (toggle && toggle.classList.contains('md-nav__toggle')) {
        toggle.checked = true;
      }
      el = el.parentElement ? el.parentElement.closest('.md-nav__item') : null;
    }
  }

  /* -----------------------------------------------------------------------
   * Sidebar scroll persistence
   * --------------------------------------------------------------------- */
  function restoreScroll() {
    var sidebar = getSidebarEl();
    if (!sidebar) return;
    var top = parseInt(localStorage.getItem(SCROLL_KEY), 10);
    if (!isNaN(top)) { sidebar.scrollTop = top; }
  }

  function persistScroll() {
    var sidebar = getSidebarEl();
    if (!sidebar) return;
    sidebar.addEventListener('scroll', function () {
      try { localStorage.setItem(SCROLL_KEY, sidebar.scrollTop); }
      catch (e) {}
    });
  }

  /* -----------------------------------------------------------------------
   * Highlight active item on instant navigation (SPA mode)
   * --------------------------------------------------------------------- */
  function onNavigation() {
    expandActiveAncestors();
  }

  /* -----------------------------------------------------------------------
   * Init
   * --------------------------------------------------------------------- */
  function init() {
    restoreState();
    expandActiveAncestors();
    persistOnChange();
    restoreScroll();
    persistScroll();

    // Hook into Material's instant navigation events
    document.addEventListener('DOMContentSwitch', onNavigation);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
