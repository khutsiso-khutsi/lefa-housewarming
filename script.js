// Interactive behaviour for the invitation page
const countdownTarget = new Date('2026-12-29T14:00:00');
const dayBox = document.getElementById('days');
const hourBox = document.getElementById('hours');
const minuteBox = document.getElementById('minutes');
const secondBox = document.getElementById('seconds');
const form = document.getElementById('rsvpForm');
const formStatus = document.getElementById('formStatus');
const giftButtons = document.querySelectorAll('.gift-card');
const giftStatusMessage = document.querySelector('.gift-note');
const storageKey = 'lefa-housewarming-gift-state';
const maxSelectionsPerGift = 3;

function updateCountdown() {
  const now = new Date();
  const difference = countdownTarget - now;

  if (difference <= 0) {
    dayBox.textContent = '00';
    hourBox.textContent = '00';
    minuteBox.textContent = '00';
    secondBox.textContent = '00';
    return;
  }

  const days = Math.floor(difference / (1000 * 60 * 60 * 24));
  const hours = Math.floor((difference / (1000 * 60 * 60)) % 24);
  const minutes = Math.floor((difference / (1000 * 60)) % 60);
  const seconds = Math.floor((difference / 1000) % 60);

  dayBox.textContent = String(days).padStart(2, '0');
  hourBox.textContent = String(hours).padStart(2, '0');
  minuteBox.textContent = String(minutes).padStart(2, '0');
  secondBox.textContent = String(seconds).padStart(2, '0');
}

function revealOnScroll() {
  const elements = document.querySelectorAll('.reveal');

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.15 }
  );

  elements.forEach((element) => observer.observe(element));
}

function validateForm(event) {
  event.preventDefault();

  const fullName = document.getElementById('fullName').value.trim();
  const guestCount = document.getElementById('guestCount').value.trim();
  const contactInfo = document.getElementById('contactInfo').value.trim();
  const attendance = document.getElementById('attendance').value;

  const emailPattern = /\S+@\S+\.\S+/;
  const phonePattern = /^\+?[0-9\s()-]{7,}$/;
  const hasValidContact = emailPattern.test(contactInfo) || phonePattern.test(contactInfo);

  if (!fullName || !guestCount || !attendance || !contactInfo) {
    showFormMessage('Please fill in all required fields.', 'error');
    return;
  }

  if (Number(guestCount) < 1) {
    showFormMessage('Guest count must be at least 1.', 'error');
    return;
  }

  if (!hasValidContact) {
    showFormMessage('Please enter a valid email address or phone number.', 'error');
    return;
  }

  showFormMessage(`Thank you, ${fullName}! We are excited to celebrate with you.`, 'success');
  form.reset();
}

function showFormMessage(message, type) {
  formStatus.textContent = message;
  formStatus.className = `form-status ${type}`;
}

function loadGiftState() {
  try {
    return JSON.parse(localStorage.getItem(storageKey)) || { selected: null, counts: {} };
  } catch (error) {
    return { selected: null, counts: {} };
  }
}

function saveGiftState(state) {
  localStorage.setItem(storageKey, JSON.stringify(state));
}

function renderGiftCards(state) {
  giftButtons.forEach((button) => {
    const giftId = button.dataset.gift;
    const count = state.counts[giftId] || 0;
    const countLabel = button.querySelector('.gift-count');
    countLabel.textContent = `${count} selected`;

    button.classList.toggle('selected', state.selected === giftId);
  });
}

function handleGiftSelection(event) {
  const button = event.currentTarget;
  const giftId = button.dataset.gift;
  const state = loadGiftState();

  if (state.selected === giftId) {
    state.counts[giftId] = Math.max(0, (state.counts[giftId] || 0) - 1);
    state.selected = null;
    giftStatusMessage.textContent = 'Selection removed. You can pick another gift whenever you like.';
    saveGiftState(state);
    renderGiftCards(state);
    return;
  }

  if (state.selected && state.selected !== giftId) {
    state.counts[state.selected] = Math.max(0, (state.counts[state.selected] || 0) - 1);
  }

  if ((state.counts[giftId] || 0) >= maxSelectionsPerGift) {
    giftStatusMessage.textContent = 'That gift has reached the current selection limit. Please choose another option.';
    return;
  }

  state.counts[giftId] = (state.counts[giftId] || 0) + 1;
  state.selected = giftId;
  giftStatusMessage.textContent = 'Your gift choice has been saved on this device.';
  saveGiftState(state);
  renderGiftCards(state);
}

updateCountdown();
setInterval(updateCountdown, 1000);
revealOnScroll();

form.addEventListener('submit', validateForm);
giftButtons.forEach((button) => button.addEventListener('click', handleGiftSelection));

const initialState = loadGiftState();
renderGiftCards(initialState);
