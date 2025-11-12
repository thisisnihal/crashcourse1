import { create } from 'zustand';
import cardsJson from './data.json';

export const useStore = create((set) => ({
  isDarkMode: typeof window !== "undefined" ? localStorage.getItem("theme") === "dark" : false,

  cardsData: (() => {
    if (typeof window === "undefined") return cardsJson;
    const saved = localStorage.getItem('cardsData');
    return saved ? JSON.parse(saved) : cardsJson;
  })(),

  initCardData: () => {
    if (typeof window === "undefined") return;

    const saved = localStorage.getItem('cardsData');
    if (saved) {
      set({ cardsData: JSON.parse(saved) });
    } else {
      localStorage.setItem('cardsData', JSON.stringify(cardsJson));
      set({ cardsData: cardsJson });
    }
  },


  toggleTheme: () =>
    set((state) => {
      const newTheme = !state.isDarkMode ? 'dark' : 'light';

      document.documentElement.classList.toggle('dark', newTheme === 'dark');
      document.documentElement.setAttribute('data-theme', newTheme);
      localStorage.setItem('theme', newTheme);

      return { isDarkMode: newTheme === 'dark' };
    }),

  setCardsData: (cardsData) => {
    set(() => ({ cardsData: cardsData }));
    localStorage.setItem('cardsData', JSON.stringify(cardsData));
  },


  removeCard: (id) =>
    set((state) => ({
      cardsData: state.cardsData.filter((c) => c.id !== id),
    })),
}));
