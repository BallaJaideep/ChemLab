import Navbar from "./Navbar";

const MainLayout = ({ children }) => {
  return (
    <>
      <Navbar />
      <main className="app-container">
        {children}
      </main>
    </>
  );
};

export default MainLayout;
