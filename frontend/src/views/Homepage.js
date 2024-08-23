import React from 'react';

function Homepage() {
  return (
    <div>
      {/* Main content of the homepage */}
      <main role="main" style={{ marginTop: 50 }}>
        {/* Jumbotron section for the primary marketing message */}
        <div className="jumbotron">
          <div className="container">
            <h1 className="display-3">Hello, world!</h1>
            <p>
              A Chat and To-Do website offers a streamlined platform combining real-time communication with task management. Users can engage in instant messaging with others, facilitating seamless interactions and discussions. The chat feature supports individual and group conversations, while the to-do component allows users to create, organize, and track their tasks efficiently.
            </p>
            <p>
              <a className="btn btn-primary btn-lg" href="#" role="button">
                Learn more »
              </a>
            </p>
          </div>
        </div>

        {/* Container for additional content */}
        <div className="container">
          {/* Row of columns */}
          <div className="row">
            {/* Column for Chat feature */}
            <div className="col-md-4">
              <h2>Chat</h2>
              <p>
                The Chat feature enables users to engage in real-time conversations with individuals or groups. It supports text-based communication, allowing users to exchange messages instantly. Features often include message notifications, user presence indicators (online/offline status), and multimedia support (e.g., images and files). The chat interface is designed to be user-friendly and responsive, ensuring smooth interactions and quick access to conversations.
              </p>
              <p>
                <a className="btn btn-secondary" href="#" role="button">
                  View details »
                </a>
              </p>
            </div>

            {/* Column for To-Do feature */}
            <div className="col-md-4">
              <h2>To-Do</h2>
              <p>
                The To-Do List feature allows users to create, manage, and prioritize tasks within a centralized system. Users can add new tasks, set deadlines, mark tasks as completed, and categorize them for better organization. The interface often includes options for setting reminders and viewing tasks in various formats (e.g., lists or calendars). This feature helps users stay organized and track their progress, enhancing productivity and ensuring that important tasks are not overlooked.
              </p>
              <p>
                <a className="btn btn-secondary" href="#" role="button">
                  View details »
                </a>
              </p>
            </div>

            {/* Column for Enjoy section */}
            <div className="col-md-4">
              <h2>Enjoy</h2>
              <p>
                Our website is designed to offer a seamless and enjoyable user experience. Whether you’re managing tasks with our intuitive To-Do List or engaging in lively conversations via our Chat feature, you’ll find an interface that's both user-friendly and visually appealing. The website combines functionality with a sleek design, ensuring that both productivity and communication are efficient and pleasant. From smooth navigation to responsive elements, every aspect is crafted to enhance your experience and make your time on the site both productive and enjoyable.
              </p>
              <p>
                <a className="btn btn-secondary" href="#" role="button">
                  View details »
                </a>
              </p>
            </div>
          </div>

          {/* Horizontal rule for separation */}
          <hr />
        </div>
        {/* /container */}
      </main>

      {/* Footer section */}
      <footer className="container">
        <p>© Company 2024 - Dylan B</p>
      </footer>
    </div>
  );
}

export default Homepage;
