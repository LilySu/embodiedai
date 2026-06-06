export function assertPseudoId(value: string): string {
  if (!/^[A-Za-z0-9_-]{8,128}$/.test(value)) {
    throw new Error("invalid_pseudo_id");
  }
  return value;
}
