# 함수형 프로그래밍

- 함수형 프로그래밍이란 무엇인가?
함수형 프로그래밍이란?
함수형 프로그래밍은 프로그래밍의 한 방법론이다
복잡한 상황을 해결하기 위해 데이터의 상태, 그리고 그 상태를 컨트롤하는 메소드를 묶어 객체끼리의 상호작용을 통해 데이터의 상태를 변경하고, 그 변경된 데이터로 현재 상태를 만들어 내는게 객체지향
객체지향은 내부 메소드가 내부 프로퍼티를 사용하는데, 따라서 이 함수는 이미 순수 함수가 아닐 것이다. 이러한 함수의 사용은 예상하지 못하는 부작용을 낳고, 쓰레드 경합에서 문제가 발생할 확률이 커서 보통은 락을 거는 방식을 사용하기도 한다. 이러한 문제를 해결하기 위해 객체지향 내부에서도 변수를 방어적 복사를 통해서 값을 변경하는 경우도 있으나, 역시 메소드 내부에서 메소드 외부의 변수를 사용하다는 점에서 순수함수로 보기 어렵다. 프로퍼티에 private final을 걸어서 변수 변경 확률을 제거하기도 한다.

복잡한 상황을 해결하기 위해 데이터를 초기화하고, 데이터를 처리하려는 액션, 그리고 그 액션을 하기 위해 필요한 계산(순수함수), 그 계산에 의해 불변성으로 새롭게 리턴되는 데이터(불변성), 그리고 그 데이터의 결과로 현재 상태를 만들어 내는게 함수형

- 함수형 프로그래밍의 장단점은 무엇인가?
스레드 경합에서 자유롭다
프로그램의 문제를 정확한 위치에서 찾기 좋다.
유지 보수가 좋아진다…? 왜…? 어떠 점에서…? 기능을 추가할 때 함수를 추가하면 되고, 기능을 바꿀땐 해당 함수의 기능만 바꾸면 됨…여기에서 말하는 함수란 순수함수, 즉 계산을 의마한다.

- 지연평가, 병렬처리, 함수의 합성, 함수의 다형성등은 함수를 객체로 보면 할 수 있다
# 객체지향은 지연평가를 못하나? 지연평가는 함수형 프로그래밍의 특성이 아니라 그냥 함수를 일급 객체로 사용하면 일어나는 효과일 뿐이다. 함수형 프로그래밍은 프로그래밍을 하는 패러다임이지, 특정 기능을 말하는 것이 아니다.

How React implements the pure functional concept
A React app component in its simplest form looks like this:
const Counter = ({ count }) => {
  return <h3>{`Count: ${count}`}</h3>;
};
This is similar to a pure function in JavaScript where a function receives an argument (in this case, a count prop) and uses the prop to render an output.
React, however, has unidirectional data flow from the parent to child component. When state data passes to a child component, it becomes an immutable prop that cannot be modified by the receiving component.
Therefore, given the same prop, this type of component always renders the same JSX. And, because of this, we can reuse the component on any page section without fear of uncertainty. This type of component is a purely functional component.
Improving app performance
React capitalizes on the pure functional concept to improve app performance. Due to the nature of React, whenever a component’s state changes, React re-renders the component and its child component, even when the state change does not directly affect the child component.
In this case, React allows us to wrap the pure functional component in React.memo to prevent unnecessary re-renders if the prop it receives never changes.
By memoizing the above pure function, we only re-render the function if the count prop changes:
const CounterComponent = React.memo(function Counter({ count }) {
  return <h3>{`Count: ${count}`}</h3>;
});
A pure functional concept in the state update
React also implements the functional concept when updating a state variable, especially when a value is based on the previous, like in the case of a counter or checkbox.
Take a look at the following code:
import { useState } from "react";
const App = () => {
  const [count, setCount] = useState(0);

  const handleClick = () => setCount(count + 1);

  return (
    // ...
  );
};

const Counter = ({ count }) => {
  // ...
};

export default App;
Here, we removed some parts of the code for brevity but expanded our previous Counter component to display a button to increment a count.
This is a familiar code for React beginners. While the code works, we can add improvements by following the functional programming concept.
Let’s focus on this part of the code:
const handleClick = () => setCount(count + 1);
Inside the setCount updater function, we use a count variable that does not pass as an argument. As we’ve learned, this is against the concept of functional programming.
One improvement React provides is passing a callback to the updater function. In this callback, we can access the previous version of the state, and from there, we can update the state value:
const handleClick = () => setCount((prev) => prev + 1);
As we can see in the setCount callback, the output computes solely on the prev input argument. That is the pure functional concept in action.
Avoiding mutating data (immutability)
When a function mutates or changes a global variable, it can lead to a bug in our program.
In functional programming, we treat mutable data structures like arrays and objects as immutable data. This means we never modify them, rather, we make a copy when passing to a function so the function can compute its output based on the copy.
Let’s revisit the following code:
const arr = [2, 4, 6];

function addElement(arr, ele) {
  return [...arr, ele];
}

console.log("modified data", addElement(arr, 8)); // Expected Output: [2, 4, 6, 8]
console.log("original data", arr); // Expected Output: [2, 4, 6]
We’ve seen this code earlier, but this time we’ll shift our focus towards the immutable functional aspect.
Here, we have a function that only uses a copy of the global variable to compute the output. We use the ES6 spread operator (…) to copy existing data into a new array and then add the new element. This way, we keep the original array input data immutable, as seen in the result.
How React handles mutable state
Since React is a reactive library, it must “react” to state changes to keep the DOM up to date. Obviously, the state value must update as well.
In React, we do not modify the state directly. Instead, we update the state using the setState() method in a class component or the updater function in a functional component.
Take a look at an excerpt from our previous code:
const handleClick = () => setCount((prev) => prev + 1);
Here, we use the updater function, setCount, to update the count number. When working with immutable data like numbers and strings, we must only pass the updated value to the updater function or invoke a callback function whenever the next state depends on the previous.
Let’s see another example that updates a string value:
import { useState } from "react";

const App = () => {
  const [person, setPerson] = useState("");

  const handleChange = (e) => {
    setPerson(e.target.value);
  };

  return (
    // ...
  );
};

export default App;
Here, we removed some of the code for brevity again.
The above code updates a form’s text field, which involves working with immutable string data. So, we must update the input field by passing the current input value to the updater function.
However, whenever we pass mutable data like an array and object, we must make a copy of the state data and compute the output based on the copy. Note that we must never modify the original state data.
In the following code, the handleChange triggers to update the state variable on every keystroke in the form:
import { useState } from "react";

const App = () => {
  const [person, setPerson] = useState({
    fName: "",
    lName: ""
  });

  const handleChange = (e) => {
    setPerson({
      ...person,
      [e.target.name]: e.target.value
    });
  };

  return (
    // ...
  );
};

export default App;
As seen in the code, we are working with a mutable object, hence, we must treat the state as immutable. Again, we do this by making a copy of the state using the ES6 spread operator and updating the affected property:
setPerson({
  ...person,
  [e.target.name]: e.target.value
});
One more improvement is ensuring that the updater function, setPerson, uses a state variable that passes as an argument of a callback function:
const handleChange = (e) => {
  setPerson((person) => ({
    ...person,
    [e.target.name]: e.target.value
  }));
};
Now, what will happen if we don’t follow this functional concept and we directly mutate the state. Obviously, we’ll experience a bug in our application.
To see a clearer picture, visit this CodeSandbox again and temporarily comment-out …person from the function, like so:
setPerson((person) => ({
  // ...person,
  [e.target.name]: e.target.value
}));
Now, by trying to write something in the form fields, the text will override each other. That is a bug that we want to prevent and we can do this by treating the state as immutable data.
Avoiding side effects
Functional programming codes are meant to be pure. A pure component in React can receive a prop as an argument and compute the output based on the input prop.
But sometimes, the component can make computations that affect and modify some state outside of its scope. These computations are called side effects. Examples of these effects include data fetching and manually manipulating the DOM.
These are tasks we often perform in our application, thus making side effects inevitable.
The snippet below is based on our previous Counter example:
const Counter = ({ count }) => {
  document.title = `Number of click: ${count}`;
  return <h3>{`Count: ${count}`}</h3>;
};
In the code, we update the document title to reflect the updated count value. This is a side-effect because we modify the DOM element that does not belong to the component, thereby making the component impure.
Performing side effects directly inside the body of a component is not allowed to avoid inconsistencies in our app. Instead, we must isolate this effect from the rendering logic. React provides us with a Hook called
useEffect to manage our side effects.
The following code implements this Hook:
const Counter = ({ count }) => {
  useEffect(() => {
    document.title = `Number of click: ${count}`;
  }, [count]);

  return <h3>{`Count: ${count}`}</h3>;
};
By placing the side effect in the React useEffect Hook means we can easily test and maintain the rendering logic.
Composition in React
In functional programming, a composition is an act of building complex functions by combining or chaining multiple smaller functions.
If we recall from the beginning of this article, we mentioned that for a given function, c and f, we can compose them to form a more complex function, demonstrated like so:
z = c(f(x))
But now, we will look at this concept of composition in the context of React.
Similar to the above functional pattern, we can build a complex component in React by injecting other components using the children prop from React. This prop also allows a component to render a varying amount of content without needing to be aware of the content ahead of time.
This gives us the flexibility to decide what goes inside a component and customize the content to get the desired output.
A good example of components that implement this concept includes Hero and Sidebar.
Building a reusable Hero component
Let’s say we want to create a Hero component that contains varying content and we can reuse it anywhere in our application.
We can start by writing the component like so:
function Hero({ children }) {
  return <section>{children}</section>;
}
The children prop used in this code allows us to inject content between the opening and closing tags of a component; in our case, a Hero component.
So, we can have something like this:
<Hero>
  <Banner>
    <h1>Home Page</h1>
    <p>This is the home page description</p>
  </Banner>
</Hero>
Now, everything in between <Hero> is considered its children prop, and thus appears between the section tags in the Hero component.
Likewise, the content inside the <Banner> JSX tag passes into the Banner component as children prop:
function Banner({ children }) {
  return (
    <div>
      {children}
      <button>Subscribe to newsletter</button>
    </div>
  );
}
The content between the <Banner> tag (that is, h1 and p) replaces children within the JSX.
In this code, the Banner component only knows about the button element because we’ve manually added the element; it doesn’t know what is coming to replace the children prop.
This makes the component reusable and flexible to customize because we have control over the content that comes in as the children. We can now decide not to render the banner heading, h1, on another page of our application.
All we must do is exclude it from the content in between the Banner tag.
By comparing the React composition to the mathematical definition, we can say the output of a Banner component becomes the input to the Hero component. In other words, the Hero is composed with the Banner component to form a whole component.



함수형 프로그래밍에 대한 나의 생각
예를 들어 객체지향에서 객체 A가 프로퍼티 배열 X를 순회하고 있었는데
다른 유저가 요청해서 객체 A의 프로터피 배열 X를 조작한다고 가정하면
이때 당연히 레이스 컨디션이 발생할 것이므로
X에 접근하려면 락을 걸고 접근해야만 한다

이러한 문제는 코드의 유지 보수를 매우 어렵게 만든다
만약 나중에 들어온 요청이 x를 조작할 때 실제 x를 조작하지 않고
x를 방어적으로 복사한 후 그 x를 조작한다면, 기존의 요청을 처리하는데 에러가 없을 것이다
이러한 일을 하는 함수를 순수 함수라고 한다

그러나 이렇게 하면 배열 x의 상태를 어떻게 저장하는가?
