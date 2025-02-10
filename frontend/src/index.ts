import { useEffect, useState } from "react";

const App = () => {
  const [greetings, setGreetings] = useState<{ message: string }[]>([]);
  const [token, setToken] = useState<string | null>(null);

  useEffect(() => {
    const storedToken = localStorage.getItem("auth_token");
    if (storedToken) {
      setToken(storedToken);
    }

    const fetchGreetings = async () => {
      if (!token) {
        console.error("No token found");
        return;
      }

      try {
        const response = await fetch(`${process.env.API_URL}/greetings`, {
          headers: {
            "Authorization": `Bearer ${token}`, // Sending token in Authorization header
          },
        });

        if (!response.ok) {
          throw new Error("Failed to fetch greetings");
        }

        const data = await response.json();
        setGreetings(data); // Assuming data is an array of objects with a 'message' field
      } catch (error) {
        console.error("There was a problem with the fetch operation:", error);
      }
    };

    fetchGreetings();
  }, [token]);

  return (
    `<div>
      <h1>Greetings:</h1>
      <ul>
        {Array.isArray(greetings) ? (
          greetings.map((greeting, index) => (
            <li key={index}>{greeting.message}</li>
          ))
        ) : (
          <li>No greetings available</li>
        )}
      </ul>
    </div>`
  ); 
}
  

export default App;
