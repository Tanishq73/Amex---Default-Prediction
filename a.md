\documentclass{article}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{hyperref}

\title{Mini Autograd Function with Backpropagation and Visualization}
\author{Tanishq Bhattacharjee}
\date{\today}

\begin{document}

\maketitle

\section*{Introduction}
This project involves the creation of a mini autograd function that computes gradients using backpropagation. The implementation supports basic mathematical operations and popular activation functions, with visualization of the computational graph using Graphviz.

\section*{Supported Operations}
The following mathematical operations are supported:

\begin{itemize}
    \item \textbf{Addition}: Computes the sum of two inputs and their gradients.
    \item \textbf{Subtraction}: Computes the difference between two inputs and their gradients.
    \item \textbf{Multiplication}: Multiplies two inputs and calculates the corresponding gradients.
    \item \textbf{Division}: Divides one input by another and computes the gradients.
\end{itemize}

\section*{Activation Functions}
The following activation functions are implemented with backpropagation:

\begin{itemize}
    \item \textbf{Tanh} (\(\tanh(x)\)): Hyperbolic tangent function.
    \item \textbf{Sigmoid} (\(\sigma(x) = \frac{1}{1 + e^{-x}}\)): A commonly used activation function in neural networks.
    \item \textbf{ReLU} (\(\text{ReLU}(x) = \max(0, x)\)): Rectified linear unit function.
\end{itemize}

\section*{Backpropagation}
The autograd system computes the derivative with respect to each operation and activation function, allowing for the calculation of gradients essential in optimization processes like gradient descent.

\section*{Visualization with Graphviz}
The computational graph for each operation and activation function is visualized using \textbf{Graphviz}. This provides an intuitive representation of the forward and backward passes through the network, helping to understand the flow of data and gradients in the system.

\section*{Usage}
To use this mini autograd system:

\begin{itemize}
    \item Include the required operations and activation functions as part of your computational graph.
    \item During the backward pass, the gradients will automatically be computed.
    \item Use Graphviz to visualize the computational graph by enabling the visualization feature in the code.
\end{itemize}

\section*{Further Details}
For more information on the implementation, usage, and examples, refer to the accompanying Python scripts.

\section*{Requirements}
Make sure to have the following installed:
\begin{itemize}
    \item \texttt{Graphviz}: For visualizing the computational graph.
    \item \texttt{NumPy}: For mathematical operations and matrix manipulations.
\end{itemize}

\section*{Contact}
If you have any questions or suggestions, feel free to reach out at \href{mailto:tanishqbhattacharjee@example.com}{tanishqbhattacharjee@example.com}.

\end{document}
