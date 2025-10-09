import { create } from 'zustand';

export const useStore = create((set) => ({
  isDarkMode: typeof window !== "undefined" ? localStorage.getItem("theme") === "dark" : false,
  user: null,
  count: 0,

  toggleTheme: () =>
    set((state) => {
      const newTheme = !state.isDarkMode ? 'dark' : 'light';

      document.documentElement.classList.toggle('dark', newTheme === 'dark');
      document.documentElement.setAttribute('data-theme', newTheme);
      localStorage.setItem('theme', newTheme);

      return { isDarkMode: newTheme === 'dark' };
    }),
  setUser: (user) => set({ user }),

  increment: () => set((state) => ({ count: state.count + 1 })),

  decrement: () => set((state) => ({ count: state.count - 1 })),
}));
