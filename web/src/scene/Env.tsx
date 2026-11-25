import { Environment, Lightformer } from '@react-three/drei'

// Image-based lighting built from a few soft "light panels" (no HDR file needed).
// Tweak the panels' colour / intensity / position to change the reflections on the model.
export default function Env({ intensity }: { intensity: number }) {
  return (
    <Environment resolution={256} environmentIntensity={intensity}>
      <Lightformer form="rect" intensity={2} color="#fff1e0" position={[3, 4, 4]} scale={[6, 4, 1]} target={[0, 0, 0]} />
      <Lightformer form="rect" intensity={1.2} color="#cfe3ff" position={[-4, 2, -3]} scale={[5, 3, 1]} target={[0, 0, 0]} />
      <Lightformer form="ring" intensity={0.8} color="#ffffff" position={[0, 6, 0]} scale={3} target={[0, 0, 0]} />
    </Environment>
  )
}
