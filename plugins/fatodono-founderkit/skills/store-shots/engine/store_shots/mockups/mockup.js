// The engine's side of every layout page, run after the page's own markup:
// fills [data-copy] elements, builds the device frames round the raws, the
// card and the badge, applies the placement, then fits the copy.
// Data (#store-shots-data): { frame, orientation, panel, status, copy: {key: text},
//   screen: {src, ratio} | null, card: {src, ratio} | null,
//   badge: {icon: svg markup} | null, cluster: [{frame, src, ratio}] | null,
//   place: {name: {css property: value}, cluster: {frame: {...}}} }.
//   ratio is the raw's height / width; cluster runs back to front.
//   orientation is the target's (portrait or landscape) and goes on the body;
//   each device takes its own from its raw. status none draws no status bar.
// Page attributes:
//   data-copy="key"     takes copy[key]; removed when the copy has none
//   data-stop           a closing . ! or ? goes in a span.stop (accent colour)
//   data-fit-lines="N"  font shrinks until the text takes at most N lines
//   data-fit-above      ...and until it ends above every device under it
//   data-stage          where the devices go (default: body)
//   data-place="name"   takes place[name] as inline style; the engine's own
//                       places are device, cluster.<frame>, card and badge
//   data-place="card"   holds an img for the card; removed without a card
//   data-place="badge"  holds a [data-icon]; removed without a badge
(async () => {
  const data = JSON.parse(document.getElementById('store-shots-data').textContent);
  const body = document.body;
  body.dataset.frame = data.frame || '';
  if (data.orientation) body.dataset.orientation = data.orientation;
  if (data.panel) body.dataset.panel = data.panel;
  if (data.status) body.dataset.status = data.status;
  const stage = document.querySelector('[data-stage]') || body;
  const images = [];

  const el = (tag, className, parent) => {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (parent) parent.append(node);
    return node;
  };

  const setText = (node, text) => {
    const stop = node.hasAttribute('data-stop') && /[.!?]$/.test(text) ? text.slice(-1) : '';
    node.textContent = stop ? text.slice(0, -1) : text;
    if (stop) el('span', 'stop', node).textContent = stop;
  };
  for (const node of document.querySelectorAll('[data-copy]')) {
    const text = (data.copy || {})[node.dataset.copy];
    if (text) setText(node, text);
    else node.remove();
  }

  // The airplane is Material's "flight" glyph.
  const AIRPLANE = '<svg class="ss-airplane" viewBox="0 0 24 24"><path d="M21 16v-2l-8-5V3.5c0-.83-.67-1.5-1.5-1.5S10 2.67 10 3.5V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5l8 2.5z"/></svg>';
  const STATUS = {
    ios: '<span class="ss-time">9:41</span><span class="ss-indicators">' + AIRPLANE +
      '<svg class="ss-signal" viewBox="0 0 18 12"><rect x="0" y="8" width="3" height="4" rx="1"/><rect x="5" y="5.5" width="3" height="6.5" rx="1"/><rect x="10" y="3" width="3" height="9" rx="1"/><rect x="15" y="0" width="3" height="12" rx="1"/></svg>' +
      '<svg class="ss-wifi" viewBox="0 0 16 12"><path d="M8 2.6c2.3 0 4.4.9 6 2.4l1.3-1.3A10.4 10.4 0 0 0 8 .7 10.4 10.4 0 0 0 .7 3.7L2 5a8.6 8.6 0 0 1 6-2.4Zm0 3.6c1.3 0 2.5.5 3.4 1.3l1.3-1.3A6.6 6.6 0 0 0 8 4.3a6.6 6.6 0 0 0-4.7 1.9l1.3 1.3c.9-.8 2.1-1.3 3.4-1.3Zm0 3.6c.4 0 .7.1 1 .4L8 11.3 7 10.2c.3-.3.6-.4 1-.4Z"/></svg>' +
      '<svg viewBox="0 0 27 12"><rect x=".5" y=".5" width="23" height="11" rx="3.5" fill="none" stroke="currentColor" opacity=".4"/><rect x="2" y="2" width="20" height="8" rx="2"/><path d="M25 4v4a2 2 0 0 0 0-4Z" opacity=".4"/></svg>' +
      '</span>',
    android: '<span class="ss-time">9:41</span><span class="ss-indicators">' + AIRPLANE +
      '<svg class="ss-wifi" viewBox="0 0 16 12"><path d="M8 11.5 0 3.2A11.6 11.6 0 0 1 8 0a11.6 11.6 0 0 1 8 3.2Z"/></svg>' +
      '<svg class="ss-signal" viewBox="0 0 12 12"><path d="M12 0v12H0Z"/></svg>' +
      '<svg viewBox="0 0 7 12"><rect x="1.5" y="0" width="4" height="1.5" rx=".5"/><rect x="0" y="1" width="7" height="11" rx="1.5"/></svg>' +
      '</span>',
  };
  // What each frame kind draws inside its screen besides the raw.
  const FRAMES = {
    iphone: { status: 'ios', cutout: 'ss-island' },
    ipad: { status: 'ios' },
    android_phone: { status: 'android', cutout: 'ss-camera' },
    android_tablet: { status: 'android' },
    mac: { titlebar: true },
  };

  const device = (kind, shot, place, member) => {
    const frame = FRAMES[kind] || {};
    const node = el('div', member ? 'ss-device ss-member' : 'ss-device', stage);
    node.dataset.kind = kind;
    node.dataset.place = place;
    if (data.status) node.dataset.status = data.status;
    node.style.setProperty('--screen-ratio', shot.ratio);
    node.dataset.orientation = shot.ratio < 1 ? 'landscape' : 'portrait';
    const screen = el('div', 'ss-screen', node);
    if (frame.titlebar) {
      const bar = el('div', 'ss-titlebar', screen);
      for (let i = 0; i < 3; i++) el('i', '', bar);
    }
    const raw = el('img', 'ss-raw', screen);
    raw.src = shot.src;
    images.push(raw.decode());
    if (frame.status && data.status !== 'none') {
      const status = el('div', `ss-status ss-status-${frame.status}`, screen);
      status.innerHTML = STATUS[frame.status];
    }
    if (frame.cutout) el('span', frame.cutout, screen);
  };
  if (data.cluster) {
    for (const member of data.cluster) device(member.frame, member, `cluster.${member.frame}`, true);
  } else if (data.screen) {
    device(data.frame, data.screen, 'device', false);
  }

  const card = document.querySelector('[data-place="card"]');
  if (card && data.card) {
    const raw = card.querySelector('img');
    raw.src = data.card.src;
    images.push(raw.decode());
  } else if (card) {
    card.remove();
  }
  const badge = document.querySelector('[data-place="badge"]');
  if (badge && data.badge) {
    const icon = badge.querySelector('[data-icon]');
    if (icon) icon.innerHTML = data.badge.icon || '';
  } else if (badge) {
    badge.remove();
  }

  for (const node of document.querySelectorAll('[data-place]')) {
    const style = node.dataset.place.split('.').reduce((at, key) => (at || {})[key], data.place);
    for (const [property, value] of Object.entries(style || {})) node.style.setProperty(property, value);
  }

  await Promise.all([document.fonts.ready, ...images]);

  const gap = window.innerHeight * 0.008;
  // The top of the highest device under [node]: one beside it is not in its way.
  const devicesTop = (node) => {
    const text = node.getBoundingClientRect();
    return Math.min(...[...document.querySelectorAll('.ss-device')]
      .map((device) => device.getBoundingClientRect())
      .filter((box) => box.left < text.right && box.right > text.left)
      .map((box) => box.top));
  };
  for (const node of document.querySelectorAll('[data-fit-lines]')) {
    const lines = Number(node.dataset.fitLines);
    const above = node.hasAttribute('data-fit-above') ? devicesTop(node) - gap : Infinity;
    let size = parseFloat(getComputedStyle(node).fontSize);
    const crowded = () => {
      const lineHeight = parseFloat(getComputedStyle(node).lineHeight);
      const box = node.getBoundingClientRect();
      return node.scrollWidth > node.clientWidth + 1 ||
        box.height > lineHeight * lines + 1 || box.bottom > above;
    };
    while (crowded() && size > 8) {
      size -= 0.5;
      node.style.fontSize = `${size}px`;
    }
  }
})();
