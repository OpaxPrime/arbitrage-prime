import { Canvas } from "@react-three/fiber";
import { OrbitControls, Sphere } from "@react-three/drei";

const ThreeDScene = () => (
  <Canvas>
    <OrbitControls />
    <ambientLight intensity={0.5} />
    <Sphere visible args={[1, 100, 100]} scale={2}>
      <meshStandardMaterial attach="material" color="#0d47a1" />
    </Sphere>
  </Canvas>
);

export default ThreeDScene;
