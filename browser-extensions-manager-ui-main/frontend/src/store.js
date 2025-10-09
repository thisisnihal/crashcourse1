import { create } from 'zustand';

export const useStore = create((set) => ({
  isDarkMode: false,    
  user: null,           
  count: 0,            

  toggleTheme: () =>
    set((state) => {
      const html = document.documentElement;
    html.classList.toggle('dark', !state.isDarkMode);
      html.setAttribute('data-theme', !state.isDarkMode ? 'dark' : 'light');
      return { isDarkMode: !state.isDarkMode };
    }),
  setUser: (user) => set({ user }),

  increment: () => set((state) => ({ count: state.count + 1 })),

  decrement: () => set((state) => ({ count: state.count - 1 })),
}));
